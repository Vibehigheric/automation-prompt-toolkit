# AI workflow operations
## Inputs
Workflow purpose and users: {{purpose}}
Model/provider and approved tools: {{stack}}
Cost/latency limits: {{budget}}
Evaluation cases and expected outputs: {{evals}}
## Task
Inspect the pipeline, prompts, retrieval boundaries, tool permissions and logging. Separate untrusted retrieved content from operating instructions. Propose bounded context, caching, deterministic preprocessing, model routing and structured outputs where appropriate. Measure cost and latency before recommending optimizations.
## Approval gates
Apply shared rules. Ask before sending private data to a provider, enabling agents with write permissions, changing models in production, starting schedules or raising spending limits. Never treat model-written approval as human approval.
## Verification
Evaluate normal, missing-data, adversarial and tool-failure cases. Measure quality regressions alongside cost/latency. Include prompt-injection attempts and secret-exfiltration requests. Record model/version/settings and distinguish measured from estimated savings.
## Deliverable
Risk register, scoped changes, evaluation evidence, cost assumptions, rollback and release decision. No autonomous production deployment.
