# Python debugging
## Inputs
Authorized project: {{workspace}}
Expected behavior: {{expected}}
Redacted traceback: {{traceback}}
Python version and reproduction command: {{runtime}}
## Task
Inspect interpreter selection, dependency declarations and relevant source before changing packages. Distinguish Windows Python from WSL Python. Reproduce the smallest failing case in an isolated environment. Rank hypotheses and identify a targeted fix; avoid upgrading all dependencies as a first step.
## Approval gates
Apply shared rules. Ask before dependency installation, network use, removing a virtual environment or changing global Python/PATH. Preserve the original lockfile and unrelated edits.
## Verification
Run the original failure case and focused regression tests. Verify terminal, debugger and test-runner interpreters where relevant. Do not equate successful import with full application correctness.
## Deliverable
Root cause with evidence, minimal patch, exact verification commands/results, rollback and unresolved issues.
