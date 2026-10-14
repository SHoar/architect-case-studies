# ADR-001: Browser talks only to a BFF

## Status

Accepted

## Context

SPAs that call many backends (or Kubernetes APIs) directly push secrets, CORS, and auth complexity into the browser—the least trusted tier—especially when coding agents can generate fetch calls freely.

## Decision

All browser traffic for platform and high-stakes products goes through a Backend-for-Frontend (BFF). The SPA never holds cluster credentials, brokerage tokens, or long-lived API keys.

## Consequences

- Clear trust boundary for security reviews
- Agents targeting the SPA cannot invent privileged calls the BFF does not expose
- Extra hop and BFF ownership cost (accepted)
