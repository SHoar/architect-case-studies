# Interview proof pack — AI-enabled Software Architect

## Target titles

- Software Architect
- Staff / Platform Engineer
- AI Platform Architect
- Solutions Architect (AI / platform)

**Avoid positioning as:** junior “AI engineer” who only ships prompts.

## One-sentence pitch

Platform-minded full-stack engineer who designs GitOps control planes and agent-safe systems—where LLMs are bounded tools, not autonomous operators.

## Artifact checklist

| Artifact | Link | Use in interview |
|----------|------|------------------|
| Trilogy case study 01 (IDP) | [01](../case-studies/01-gitops-idp-platform.md) | System design whiteboard warm-up |
| Trilogy case study 02 (agent-safe) | [02](../case-studies/02-agent-safe-product.md) | Safety / HITL deep dive |
| Trilogy case study 03 (kdev) | [03](../case-studies/03-kdev-companion.md) | Tooling-for-agents story |
| RFC BFF + GitOps | [RFC-001](../rfc/001-bff-gitops-for-agents.md) | Leadership / influence sample |
| SLO & cost narrative | [ops](../ops/slo-cost-idp-rag.md) | Production readiness |
| Eval harness demo | [demo](../demos/agent-eval-harness/) | Live 5-minute terminal demo |
| Public AI microservice | [Wedding-AI](https://github.com/SHoar/Wedding-AI) | Shipping evidence |
| Portfolio | https://shoar.github.io/portfolio | Recruiter screen |

## Live demo script (5–7 minutes)

1. `cd demos/agent-eval-harness && pip install -e .`
2. `agent-eval matrix` — show fail-closed permission table
3. `agent-eval run --suite fixtures/suite.json` — all cases PASS
4. Open one JSONL trace — point at `outcome: refuse` for `cluster_apply`
5. Tie back to RFC: agents propose PRs; they do not apply

Optional stretch: walk the IDP intent flow on a whiteboard (propose → CI → Argo → Ready).

## Talk targets

- **RVNUG** — “Making agents safe around Kubernetes: exit codes, GitOps, and BFFs”
- **Carolina Codes** — “Policy over prompts: architecting HITL agentic systems”

## Pin strategy (GitHub)

1. `architect-case-studies` (this repo)
2. `Wedding-AI`
3. `job-search-pipelines`
4. `portfolio`
5. (Optional) one learning highlight — not a fork without contribution story
