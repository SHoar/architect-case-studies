# LLM as narrator, not decision-maker

## Pattern

```
User intent → Deterministic policy → (optional) LLM narration → Human gate → Effector
```

The LLM never sits alone on the path to irreversible effects.

## Why

- Policies are unit-testable; prompts are not a control.
- Regulated domains need explainability that cites rules, not vibes.
- Agents that “negotiate” past safety text will; code gates will not.

## Implementation sketch

1. Compute recommendation struct in code (`allowed`, `reasons[]`, `orders[]`).
2. Pass struct to LLM with instruction: *explain only; do not invent orders*.
3. UI shows structured orders for human approval; submit API rejects if policy hash mismatches.

## Related

- [ADR-004](../adrs/ADR-004-policy-over-llm.md)
- [Case study 02](../case-studies/02-agent-safe-product.md)
