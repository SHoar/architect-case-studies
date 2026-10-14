# GitHub profile setup (manual steps)

`gh` may lack the `user` scope for bio updates, and profile pins are easiest in the UI.

## Bio (one sentence)

```text
Platform / AI systems architect. GitOps control planes & agent-safe systems—LLMs as bounded tools, not autonomous operators.
```

Or via CLI after `gh auth refresh -h github.com -s user`:

```bash
gh api user -X PATCH -f bio='Platform / AI systems architect. GitOps control planes & agent-safe systems—LLMs as bounded tools, not autonomous operators.'
```

## Pin order (max 6)

1. [architect-case-studies](https://github.com/SHoar/architect-case-studies) — trilogy
2. [Wedding-AI](https://github.com/SHoar/Wedding-AI) — shipped AI microservice
3. [job-search-pipelines](https://github.com/SHoar/job-search-pipelines) — AI pipelines
4. [portfolio](https://github.com/SHoar/portfolio) — positioning site
5. [helloworld-pubsub-expressjs-rabbitmq](https://github.com/SHoar/helloworld-pubsub-expressjs-rabbitmq) — event-driven baseline
6. Optional: one learning highlight with a clear contribution story (avoid forks without commits)

**UI:** GitHub profile → Customize your pins.

## Topics on architect-case-studies

Suggested topics: `architecture`, `platform-engineering`, `gitops`, `agentic-ai`, `adrs`, `kubernetes`
