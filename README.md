# Automation Prompt Toolkit

Human-supervised templates for automation design, Python debugging, Windows diagnostics, Git workflows and AI operations. These are drafting aids, not autonomous repair tools or guaranteed safety controls.

## Use

1. Read COMMON_RULES.md and the chosen file under prompts/.
2. Replace the {{placeholders}} with minimal, redacted task context.
3. Give both texts to your chosen assistant, review its proposed actions and approve only scoped changes.
4. Validate the actual result independently. Do not run returned commands blindly.

The examples in examples/acceptance-cases.json are manual evaluation scenarios, not executed repairs or model-performance results. Run `python validate.py` to check package structure and `python -m unittest -v` for validator tests. These checks do not evaluate prompt effectiveness.

## Related freelance services

Contact: [IAMDIGITAL.ENT@GMAIL.COM](mailto:IAMDIGITAL.ENT@GMAIL.COM?subject=Automation%20Prompt%20Toolkit%20Inquiry).

- I will tailor automation prompts to your repeatable business workflow.
- I will build a Python debugging prompt and verification checklist.
- I will create a Windows troubleshooting prompt with approval boundaries.
- I will design Git workflow prompts that preserve uncommitted work.
- I will develop AI operations prompts with evaluation and cost controls.

Paid scope should specify one workflow, supported tools, input examples, acceptance cases, revision limit and handover. Model subscriptions, repairs, hosting, integration and ongoing support are not included unless separately agreed. No guaranteed accuracy, token savings, revenue or platform approval.

Do not submit private logs, credentials or customer records in public issues. Public issues are for this toolkit's defects. Business inquiries use the email above without sensitive attachments.

## License and limits

Limited private evaluation under LICENSE.txt; not an open-source license. Production or paid-client reuse requires separate written permission, subject to statutory and GitHub platform rights. Richard Jones reserves only rights legally held. AI-assisted materials may have limited copyright protection. The custom license is a draft for legal review, not a guarantee of enforceability.

No client work, successful repairs or model evaluations are claimed by this publication. No network calls or third-party dependencies are needed to validate the package.
