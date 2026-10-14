# ADR-007: Exit codes are the automation API

## Status

Accepted

## Context

Agents and CI need unambiguous outcomes. Parsing natural language or partial JSON from tools is brittle.

## Decision

Define stable exit codes (pass / fail / unknown / policy refuse / timeout). Prefer `--json` structured stdout for details.

## Consequences

- Simple branching in skills and scripts
- Requires documentation discipline when adding codes
