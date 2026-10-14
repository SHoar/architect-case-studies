# ADR-006: Workstation companion, not in-cluster operator

## Status

Accepted (MVP)

## Context

In-cluster operators expand blast radius and require CRDs, RBAC, and upgrade paths before the product thesis is proven.

## Decision

Ship a local CLI + policy files first. No Deployment/CRD/operator in-cluster for MVP. Apply/change modes stay unimplemented until explicitly designed.

## Consequences

- Faster iteration and safer demos
- Limited multi-user fleet management (deferred)
