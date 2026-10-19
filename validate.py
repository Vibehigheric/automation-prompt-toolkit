"""Static structure checks only; does not execute prompts or contact models."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
NAMES = ('automation', 'python-debug', 'windows-repair', 'git-workflow', 'ai-ops')

def validate(root=ROOT):
    errors = []
    for name in NAMES:
        path = root / 'prompts' / (name + '.md')
        if not path.is_file():
            errors.append('Missing template: ' + name)
            continue
        text = path.read_text(encoding='utf-8')
        for heading in ('## Inputs', '## Task', '## Approval gates', '## Verification', '## Deliverable'):
            if heading not in text:
                errors.append(name + ': missing ' + heading)
    for name in ('COMMON_RULES.md', 'README.md', 'LICENSE.txt'):
        if not (root / name).is_file():
            errors.append('Missing: ' + name)
    try:
        cases = json.loads((root / 'examples/acceptance-cases.json').read_text(encoding='utf-8'))
        if not isinstance(cases, list) or len(cases) != 5:
            errors.append('Expected five manual evaluation cases')
        elif {c.get('category') for c in cases} != set(NAMES):
            errors.append('Evaluation categories mismatch')
        elif not all(c.get('scenario') and c.get('expected') for c in cases):
            errors.append('Incomplete evaluation case')
    except (OSError, ValueError, AttributeError, TypeError):
        errors.append('Invalid evaluation cases')
    return errors

if __name__ == '__main__':
    errors = validate()
    print(json.dumps({'static_validation': 'FAIL' if errors else 'PASS',
                      'model_evaluation': 'NOT_RUN', 'errors': errors}, indent=2))
    raise SystemExit(bool(errors))
