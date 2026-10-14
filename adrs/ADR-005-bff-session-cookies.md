# ADR-005: httpOnly session cookies at the BFF

## Status

Accepted

## Context

Storing OAuth/access tokens in `localStorage` makes XSS catastrophic and invites agent-generated client code to mishandle secrets.

## Decision

BFF establishes httpOnly, Secure, SameSite session cookies. Frontend never sees raw provider tokens.

## Consequences

- CSRF protections and cookie hygiene required
- Aligns with BFF-only browser ADR
