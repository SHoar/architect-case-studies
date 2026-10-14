# Agent eval harness (minimal)

Public demo of **permission matrices**, **refusal paths**, **success criteria**, and **trace events**—without calling a paid LLM by default.

## Run

```bash
cd demos/agent-eval-harness
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
agent-eval run --suite fixtures/suite.json
agent-eval matrix
```

## What it shows

1. Tools are allow/deny by role (`observer` vs `proposer`).
2. Denied tools emit `refuse` outcomes (not exceptions swallowed as success).
3. Each case has explicit success criteria checked against the trace.
4. JSONL trace is suitable for later OpenTelemetry export.

## Extend

- Point `FakeLLM` at a real provider behind an env flag.
- Add cost fields (`tokens_in`, `tokens_out`) per step.
- Wire Wedding-AI `/ask` as a live case once credentials exist.
