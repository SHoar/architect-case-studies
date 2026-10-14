# ADR-004: Deterministic policy decides; LLM narrates

## Status

Accepted

## Context

LLMs are persuasive and non-deterministic. Using them as the sole decision-maker for irreversible actions is an unacceptable control failure.

## Decision

Business rules and safety policy live in deterministic code. The LLM may explain, summarize, or draft—never alone approve mutations.

## Consequences

- Testable recommendations
- Clear labeling (“analysis/education, not advice”)
- Agents cannot “talk their way” past gates
