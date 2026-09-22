---
name: ai-automation-skill
description: Use for AI agents, LangChain, AutoGPT-style automation, crewAI, tool orchestration, task planning, multi-agent workflows, retrieval, memory, human-in-the-loop controls, evaluation, and automation safety. Trigger when designing or implementing autonomous workflows, LLM tooling, agent loops, or AI-assisted operations.
---

# AI Automation Skill

Use this skill to design useful automation with explicit boundaries and verification.

Reference repositories:
- https://github.com/langchain-ai/langchain
- https://github.com/Significant-Gravitas/AutoGPT
- https://github.com/joaomdmoura/crewAI

## Workflow

1. Define the task, allowed actions, data sources, stop conditions, and human approval points.
2. Choose the simplest architecture: direct tool call, workflow, retrieval pipeline, single agent, or multi-agent system.
3. Make tool inputs and outputs typed where possible.
4. Add guardrails for permissions, secrets, rate limits, retries, and irreversible actions.
5. Persist only useful state: task IDs, decisions, outputs, costs, and audit events.
6. Evaluate with deterministic fixtures before relying on live autonomy.
7. Prefer observable workflows over opaque autonomous loops.

## Framework Guidance

- LangChain: use focused chains or tool-calling agents when orchestration adds value; keep prompts and tools versioned.
- AutoGPT-style systems: require explicit budgets, stop conditions, and operator review for external actions.
- crewAI: use multiple agents only when roles have genuinely different context or tools.

## Review Checklist

- The workflow can stop safely.
- Tool permissions are least-privilege.
- Outputs are validated before being trusted.
- Cost and failure modes are visible.
- Human approval exists for destructive or high-impact actions.
