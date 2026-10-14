# Threat modeling when agents touch infrastructure

Agents change the threat model: they are tireless, literal, and happy to retry destructive actions.

## Assets

- Cluster credentials and kubeconfigs
- Git deploy keys / CI tokens
- Object metadata that might contain secrets (annotations, ConfigMaps)
- Human attention (alert fatigue from agent loops)

## STRIDE-style notes for agent tooling

| Category | Agent-specific twist | Control pattern |
|----------|----------------------|-----------------|
| Spoofing | Agent uses stale or wrong context identity | Short-lived creds; explicit identity in every tool |
| Tampering | Agent “fixes” YAML in ways policy forbids | Schema validation + GitOps PR only |
| Repudiation | No trail of who/what invoked apply | Audit every tool call; exit codes + logs |
| Info disclosure | Cluster objects pasted into prompts | Sanitize exports; redact before LLM |
| DoS | Observe loops hammering API server | Rate limits, timeouts, exit code 4 |
| Elevation | Skill claims “temporary” write | Separate read vs write tool sets; write off by default |

## Takeaway

If your agent stack cannot refuse (exit code / HTTP 403) as easily as it can act, it is not production-ready.
