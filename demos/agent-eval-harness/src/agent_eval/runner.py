"""Run eval cases against a fake agent that respects the permission matrix."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from .permissions import DEFAULT_MATRIX, Decision, PermissionMatrix
from .trace import Outcome, Trace


ToolFn = Callable[[dict[str, Any]], dict[str, Any]]


def _tool_list_blueprints(_: dict[str, Any]) -> dict[str, Any]:
    return {"blueprints": ["namespace", "application"]}


def _tool_get_claim_status(args: dict[str, Any]) -> dict[str, Any]:
    return {"name": args.get("name", "demo"), "ready": True}


def _tool_propose_claim(args: dict[str, Any]) -> dict[str, Any]:
    return {"pr_url": f"https://git.example/pr/{args.get('name', 'demo')}"}


def _tool_cluster_apply(_: dict[str, Any]) -> dict[str, Any]:
    raise RuntimeError("cluster_apply must never execute")


TOOLS: dict[str, ToolFn] = {
    "list_blueprints": _tool_list_blueprints,
    "get_claim_status": _tool_get_claim_status,
    "propose_claim": _tool_propose_claim,
    "cluster_apply": _tool_cluster_apply,
}


@dataclass
class CaseResult:
    case_id: str
    passed: bool
    reasons: list[str]
    trace: Trace


def invoke_tool(
    role: str,
    tool: str,
    args: dict[str, Any],
    trace: Trace,
    matrix: PermissionMatrix = DEFAULT_MATRIX,
) -> dict[str, Any]:
    decision = matrix.decide(role, tool)
    if decision is Decision.DENY:
        trace.add(
            "tool_call",
            tool=tool,
            role=role,
            outcome=Outcome.REFUSE,
            detail={"reason": "permission_denied", "args": args},
        )
        return {"refused": True, "reason": "permission_denied"}

    try:
        result = TOOLS[tool](args)
    except Exception as exc:  # noqa: BLE001 — surface as fail outcome
        trace.add(
            "tool_call",
            tool=tool,
            role=role,
            outcome=Outcome.FAIL,
            detail={"error": str(exc)},
        )
        return {"error": str(exc)}

    trace.add(
        "tool_call",
        tool=tool,
        role=role,
        outcome=Outcome.OK,
        detail={"result": result},
    )
    return result


def evaluate_criteria(trace: Trace, criteria: list[dict[str, Any]]) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    ok = True
    for rule in criteria:
        kind = rule.get("type")
        if kind == "must_refuse_tool":
            tool = rule["tool"]
            refused = any(
                e.tool == tool and e.outcome == Outcome.REFUSE for e in trace.events
            )
            if not refused:
                ok = False
                reasons.append(f"expected refuse for tool {tool}")
        elif kind == "must_allow_tool":
            tool = rule["tool"]
            allowed = any(
                e.tool == tool and e.outcome == Outcome.OK for e in trace.events
            )
            if not allowed:
                ok = False
                reasons.append(f"expected allow for tool {tool}")
        elif kind == "must_not_ok_tool":
            tool = rule["tool"]
            bad = any(e.tool == tool and e.outcome == Outcome.OK for e in trace.events)
            if bad:
                ok = False
                reasons.append(f"tool {tool} must never succeed")
        else:
            ok = False
            reasons.append(f"unknown criterion type: {kind}")
    return ok, reasons


def run_case(case: dict[str, Any], matrix: PermissionMatrix = DEFAULT_MATRIX) -> CaseResult:
    case_id = case["id"]
    role = case["role"]
    trace = Trace(case_id=case_id)
    trace.add("case_start", detail={"role": role, "goal": case.get("goal")})

    for step in case.get("steps", []):
        invoke_tool(role, step["tool"], step.get("args", {}), trace, matrix)

    passed, reasons = evaluate_criteria(trace, case.get("success_criteria", []))
    trace.add(
        "case_end",
        outcome=Outcome.OK if passed else Outcome.FAIL,
        detail={"passed": passed, "reasons": reasons},
    )
    return CaseResult(case_id=case_id, passed=passed, reasons=reasons, trace=trace)


def run_suite(suite_path: Path, out_dir: Path | None = None) -> list[CaseResult]:
    suite = json.loads(suite_path.read_text(encoding="utf-8"))
    results = [run_case(case) for case in suite["cases"]]
    if out_dir is not None:
        out_dir.mkdir(parents=True, exist_ok=True)
        for result in results:
            result.trace.write_jsonl(out_dir / f"{result.case_id}.jsonl")
        summary = {
            "passed": sum(1 for r in results if r.passed),
            "failed": sum(1 for r in results if not r.passed),
            "cases": [
                {"id": r.case_id, "passed": r.passed, "reasons": r.reasons}
                for r in results
            ],
        }
        (out_dir / "summary.json").write_text(
            json.dumps(summary, indent=2) + "\n", encoding="utf-8"
        )
    return results
