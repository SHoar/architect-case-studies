# ADR-003: Contract-first shared DTOs

## Status

Accepted

## Context

Portal, BFF, and docs drift when each invents shapes independently—worse when agents generate clients from guesswork.

## Decision

Shared contracts package (e.g. Zod / OpenAPI) is the source of truth. Apps import types; CI fails on contract breakage.

## Consequences

- Safer codegen and agent tooling
- Versioning discipline required (see notes on compatibility policy)
