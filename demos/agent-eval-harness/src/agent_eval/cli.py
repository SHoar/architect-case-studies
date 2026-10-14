"""CLI entrypoint for agent-eval."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .permissions import render_matrix
from .runner import run_suite


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="agent-eval")
    sub = parser.add_subparsers(dest="cmd", required=True)

    run_p = sub.add_parser("run", help="Run an eval suite")
    run_p.add_argument("--suite", type=Path, required=True)
    run_p.add_argument("--out", type=Path, default=Path("out"))

    sub.add_parser("matrix", help="Print the default permission matrix")

    args = parser.parse_args(argv)

    if args.cmd == "matrix":
        print(render_matrix())
        return 0

    if args.cmd == "run":
        results = run_suite(args.suite, args.out)
        failed = [r for r in results if not r.passed]
        for r in results:
            mark = "PASS" if r.passed else "FAIL"
            extra = f" — {', '.join(r.reasons)}" if r.reasons else ""
            print(f"{mark} {r.case_id}{extra}")
        print(f"\n{len(results) - len(failed)}/{len(results)} passed; traces in {args.out}/")
        return 1 if failed else 0

    return 2


if __name__ == "__main__":
    sys.exit(main())
