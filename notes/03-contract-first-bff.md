# Contract-first BFF for agent platforms

## Compatibility policy (starter)

1. **Additive changes** to response DTOs are minor; clients must ignore unknown fields.
2. **Renames/removals** require a major version or dual-publish window (≥1 release).
3. **Tool schemas** exposed to agents are versioned (`tools/v1/...`); breaking tool args = new tool id.
4. CI runs contract tests on every PR; generated OpenAPI is an artifact, not hand-edited.

## Why agents need this more than humans

Humans adapt to a broken field name. Agents cache schemas and will call deleted endpoints forever—or invent parameters. Contracts + versioned tools keep agent platforms boring and reliable.

## Related

- [ADR-001](../adrs/ADR-001-bff-only-browser.md)
- [ADR-003](../adrs/ADR-003-contract-first-dtos.md)
- [RFC-001](../rfc/001-bff-gitops-for-agents.md)
