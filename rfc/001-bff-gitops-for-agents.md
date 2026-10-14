# RFC-001: Why BFF-only + GitOps claims beat direct cluster writes for agents

**Status:** Proposed for portfolio / platform discussions  
**Author:** Sean Hoar  
**Date:** 2026-10-13

## Summary

Coding agents and IDP portals must not hold live Kubernetes write credentials. Intent should flow: **UI/agent → BFF → Git PR → CI → merge → GitOps sync → Crossplane/controllers**. Direct apply is reserved for break-glass humans with audited break-glass workflows—not default agent tools.

## Motivation

1. Agents optimize for task completion, not change management.
2. Live apply skips review, policy gates, and reproducible history.
3. BFF shrinks the browser/agent attack surface to an explicit tool catalog.

## Alternatives considered

| Option | Pros | Cons |
|--------|------|------|
| A. Agent with kubeconfig write | Fast | Unbounded blast radius |
| B. Portal calls Crossplane API | Convenient UX | Still bypasses Git; hard to audit |
| **C. BFF + GitOps claims (chosen)** | Reviewable, revertible, CI-gated | Slightly higher latency |
| D. In-cluster AI operator | Centralized | Huge trust + upgrade burden |

## Detailed design

1. **Tool catalog** for agents: `propose_claim`, `get_claim_status`, `list_blueprints` — no `apply`.
2. **BFF** validates schema, authZ, and rate limits; opens PR.
3. **CI** runs schema + policy checks on the PR.
4. **Argo** syncs only `main`.
5. **Status UI** reconciles from cluster read APIs via BFF (read path may be live; write path is Git).

## Rollout

1. Mock mode for UX without cluster.
2. Lite control plane for golden path.
3. Prod: same contracts; stronger IdP and audit sinks.

## Open questions

- How long to keep failed proposal branches?
- Should agents be allowed to reopen PRs after CI comments?
- Break-glass human apply: which role + which audit ticket fields?

## Decision ask

Adopt option C as the default architecture for any agent- or portal-driven infrastructure mutation in platform work.
