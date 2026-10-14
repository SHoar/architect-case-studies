"""Tool permission matrix: role → tool → allow|deny."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Decision(str, Enum):
    ALLOW = "allow"
    DENY = "deny"


@dataclass(frozen=True)
class PermissionMatrix:
    """Explicit allow/deny table. Missing entries are deny (fail-closed)."""

    table: dict[str, dict[str, Decision]]

    def decide(self, role: str, tool: str) -> Decision:
        role_table = self.table.get(role, {})
        return role_table.get(tool, Decision.DENY)


DEFAULT_MATRIX = PermissionMatrix(
    table={
        "observer": {
            "list_blueprints": Decision.ALLOW,
            "get_claim_status": Decision.ALLOW,
            "propose_claim": Decision.DENY,
            "cluster_apply": Decision.DENY,
        },
        "proposer": {
            "list_blueprints": Decision.ALLOW,
            "get_claim_status": Decision.ALLOW,
            "propose_claim": Decision.ALLOW,
            "cluster_apply": Decision.DENY,
        },
        "break_glass": {
            "list_blueprints": Decision.ALLOW,
            "get_claim_status": Decision.ALLOW,
            "propose_claim": Decision.ALLOW,
            # Still deny by default — break-glass is a human process, not an agent tool.
            "cluster_apply": Decision.DENY,
        },
    }
)


def render_matrix(matrix: PermissionMatrix = DEFAULT_MATRIX) -> str:
    tools = sorted({t for role in matrix.table.values() for t in role})
    roles = sorted(matrix.table)
    header = "| role \\ tool | " + " | ".join(tools) + " |"
    sep = "|---|" + "|".join(["---"] * len(tools)) + "|"
    rows = []
    for role in roles:
        cells = [matrix.decide(role, tool).value for tool in tools]
        rows.append(f"| {role} | " + " | ".join(cells) + " |")
    return "\n".join([header, sep, *rows])
