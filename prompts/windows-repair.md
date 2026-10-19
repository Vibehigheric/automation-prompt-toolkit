# Windows development-workspace diagnosis
## Inputs
Windows/tool versions: {{versions}}
Redacted error and recent change: {{symptom}}
Allowed scope and administrator restrictions: {{scope}}
Permitted downtime: {{downtime}}
## Task
Begin with read-only checks of relevant tool availability, process/service status and narrowly scoped logs. Distinguish tool presence from operational health. Diagnose VS Code, Python, Git, Docker or WSL only as relevant. Inspect existing settings before proposing edits.
## Approval gates
Apply shared rules. Do not change WSL networking, restart WSL/Docker, unregister a distro, delete volumes, reset Windows, alter execution policy or disable security controls without explicit approval for that action. Respect a prior refusal. Never treat a request to diagnose as approval to restart.
## Verification
Define a safe before/after smoke test. Confirm configuration, data preservation and application behavior separately. Show commands not run and blocked steps.
## Deliverable
Evidence-led diagnosis, narrowly scoped repair proposal, downtime impact, backup/rollback, acceptance test results.
