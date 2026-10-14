"""Simple JSONL-friendly trace events for agent runs."""

from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any


class Outcome(str, Enum):
    OK = "ok"
    REFUSE = "refuse"
    FAIL = "fail"


@dataclass
class TraceEvent:
    ts: float
    kind: str
    tool: str | None = None
    role: str | None = None
    outcome: Outcome | None = None
    detail: dict[str, Any] = field(default_factory=dict)

    def to_json(self) -> str:
        payload = asdict(self)
        if self.outcome is not None:
            payload["outcome"] = self.outcome.value
        return json.dumps(payload, sort_keys=True)


@dataclass
class Trace:
    case_id: str
    events: list[TraceEvent] = field(default_factory=list)

    def add(self, kind: str, **kwargs: Any) -> TraceEvent:
        event = TraceEvent(ts=time.time(), kind=kind, **kwargs)
        self.events.append(event)
        return event

    def write_jsonl(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as fh:
            for event in self.events:
                fh.write(event.to_json() + "\n")
