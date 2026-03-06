import os
import yaml
import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

MANDATORY_FILES = [
    'README.md',
    'PULL_REQUEST_TEMPLATE.md',
    '.github/workflows/ci.yml',
    'docs/ONBOARDING.md',
]


def read_file(path):
    full = os.path.join(ROOT, path)
    if not os.path.exists(full):
        return None
    with open(full, 'r', encoding='utf-8') as f:
        return f.read()


@pytest.mark.parametrize('path', MANDATORY_FILES)
def test_mandatory_files_exist(path):
    assert read_file(path) is not None, f"Mandatory file missing: {path}"


def test_ci_contains_test_and_lint():
    content = read_file('.github/workflows/ci.yml')
    assert content is not None, 'ci.yml missing'
    # simple string checks
    assert 'pytest' in content or 'python -m pytest' in content, 'ci.yml must run pytest'
    assert 'flake8' in content or 'ruff' in content or 'black' in content or 'eslint' in content, 'ci.yml must run a linter (flake8/ruff/black/eslint)'


def test_ci_triggers_on_pr_or_push():
    content = read_file('.github/workflows/ci.yml')
    # quick checks without full yaml parsing
    assert 'pull_request' in content or 'push' in content, 'ci.yml should trigger on pull_request or push'


def test_pr_template_has_checklist():
    content = read_file('PULL_REQUEST_TEMPLATE.md')
    assert content is not None, 'PR template missing'
    assert '## Checklist' in content or '- [ ]' in content, 'PR template should include a checklist'
    assert 'run tests' in content.lower() or 'ci' in content.lower(), 'PR template should ask to run CI/tests and link issue'


def test_onboarding_has_run_tests_and_linters():
    content = read_file('docs/ONBOARDING.md')
    assert content is not None, 'Onboarding doc missing'
    lower = content.lower()
    assert 'run tests' in lower or 'pytest' in lower, 'Onboarding should explain how to run tests'
    assert 'lint' in lower or 'flake8' in lower or 'ruff' in lower or 'eslint' in lower, 'Onboarding should explain how to run linters'
