# ADR-008: Optional MCP adapter wraps the same CLI

## Status

Accepted (design)

## Context

MCP is a convenient agent interface, but a separate mutate-capable MCP server would invent a second privilege path.

## Decision

If MCP is added, it must wrap the **same** deterministic companion commands and inherit policy refusals. No parallel “smart apply” tool.

## Consequences

- One security story
- Slightly less “magic” than unconstrained MCP toolkits (intentional)
