# Git workflow and recovery
## Inputs
Repository and permitted branch: {{repository}}
Requested outcome: {{goal}}
Known uncommitted work: {{changes}}
Allowed remote actions: {{remote_scope}}
## Task
Inspect status, current branch, remotes and relevant diffs before proposing commands. Preserve unrelated edits. Identify whether the issue is authentication, remote URL, merge state, branch divergence or local configuration. Keep credentials with the user; use approved credential helpers.
## Approval gates
Apply shared rules. Never hard-reset, clean untracked files, overwrite work, force-push, delete branches or publish private code without explicit scoped authorization. Do not stash user changes silently. Review staged paths and secrets before a commit or push.
## Verification
Compare pre/post status and intended diff. Verify remote branch/commit only after an authorized push. Local commit success is not proof remote publication succeeded.
## Deliverable
Repository state, safe commands, approval points, conflict-resolution plan, validation and recovery steps.
