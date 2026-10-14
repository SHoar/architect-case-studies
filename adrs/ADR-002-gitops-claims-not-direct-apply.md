# ADR-002: Propose GitOps claims; do not direct-apply

## Status

Accepted

## Context

Portals and agents that `kubectl apply` or create Crossplane claims via live API bypass review, CI, and drift detection.

## Decision

User/agent intent becomes a **pull request** of claim YAML. Only merged `main` is synced by Argo CD to Crossplane. Open PR heads are never applied.

## Consequences

- Auditability and rollback via Git
- Slightly slower feedback than live apply (mitigated with fast CI + status UI)
- Requires platform investment in claim UX and status reconciliation
