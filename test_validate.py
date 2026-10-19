from pathlib import Path
import shutil
import tempfile
import unittest
from validate import validate, ROOT

class Tests(unittest.TestCase):
    def test_complete_package(self):
        self.assertEqual(validate(), [])

    def test_missing_template(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / 'prompts', root / 'prompts')
            (root / 'prompts/git-workflow.md').unlink()
            self.assertIn('Missing template: git-workflow', validate(root))

    def test_missing_heading(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'prompts').mkdir()
            (root / 'prompts/automation.md').write_text('# Incomplete', encoding='utf-8')
            self.assertIn('automation: missing ## Approval gates', validate(root))

if __name__ == '__main__':
    unittest.main()
