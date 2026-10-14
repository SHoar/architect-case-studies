# Architect Case Studies

[![Architecture](https://img.shields.io/badge/focus-architecture%20%2F%20platform%20%2F%20agents-0A7EA4)](./case-studies/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

Public, sanitized architecture notes for an **AI-enabled / agentic Software Architect** portfolio.

> Platform-minded full-stack engineer who designs GitOps control planes and agent-safe systems—where LLMs are bounded tools, not autonomous operators.

## Architect Trilogy

| # | Case study | Theme |
|---|------------|--------|
| 1 | [GitOps IDP / Crossplane platform](./case-studies/01-gitops-idp-platform.md) | Control plane, BFF-only browser, propose→PR→Argo→Crossplane |
| 2 | [Agent-safe product architecture](./case-studies/02-agent-safe-product.md) | HITL, policy-over-LLM, threat model, fail-closed defaults |
| 3 | [Deterministic K8s companion for agents](./case-studies/03-kdev-companion.md) | Exit-code contracts, no auto model calls, MCP/skill boundaries |

Each case study includes: context diagram, ADRs, threat-model excerpt, and “what changes at company scale.”

## Architecture notes

- [Threat modeling agent-touched infra](./notes/01-threat-modeling-agent-infra.md)
- [LLM as narrator, not decision-maker](./notes/02-llm-narrator-not-decider.md)
- [Contract-first BFF for agent platforms](./notes/03-contract-first-bff.md)

## Hire-loop artifacts

- **RFC:** [Why BFF-only + GitOps claims beat direct cluster writes for agents](./rfc/001-bff-gitops-for-agents.md)
- **Ops:** [SLOs, failure domains, and cost for IDP + RAG stacks](./ops/slo-cost-idp-rag.md)
- **Demo:** [Agent eval harness + permission matrix](./demos/agent-eval-harness/)

## Proof pack & focus

- [Interview proof pack](./proof/PROOF_PACK.md) — roles, demos, talk targets
- [GitHub profile setup](./proof/GITHUB_PROFILE_SETUP.md) — bio + pin checklist
- [90-day focus rule](./FOCUS_90_DAYS.md) — no net-new domains; finish and narrate the trilogy

## Related public work

- [Wedding-AI](https://github.com/SHoar/Wedding-AI) — LangChain + PydanticAI microservice pattern
- [job-search-pipelines](https://github.com/SHoar/job-search-pipelines) — AI matching pipelines
- [Portfolio](https://shoar.github.io/portfolio)

## License

MIT — see [LICENSE](./LICENSE). Case studies describe patterns; they intentionally omit private credentials, personal financial data, and proprietary client material.
