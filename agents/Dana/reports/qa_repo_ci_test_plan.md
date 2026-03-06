QA Plan: Repo skeleton & CI checklist

Objective
- Validate that the repository skeleton and CI artifacts created by the backend owner (Marcus, Task 220) meet the team's onboarding, quality, and automation requirements so other streams can start work without blockers.

Scope
- Files and docs: README.md, CONTRIBUTING.md, PULL_REQUEST_TEMPLATE.md, docs/ONBOARDING.md, .gitignore, CODE_OF_CONDUCT.md, .github/ISSUE_TEMPLATE/*
- CI workflows: .github/workflows/ci.yml (tests + lint), .github/workflows/coverage.yml, .github/workflows/build.yml (optional), sample GitHub Actions templates
- CI checklist: CI must run lint, unit tests, coverage reporting, and fail fast on critical errors
- Onboarding artifacts: Developer setup steps, local test commands, environment variable guidance

Acceptance criteria (measurable)
- All expected files exist in repo root or .github/* paths
- CI workflows include steps to run linters, tests (pytest), and produce coverage reports
- A PR template exists that reminds authors to run CI and link the epic/issue
- Onboarding doc contains at minimum: repo layout, how to run tests locally, how to run linters, how to add a new workflow
- Automated tests (QA) must pass locally for existence checks and content smoke tests

Test strategy
- Equivalence partitioning: existence vs. non-existence of files; presence vs. absence of required CI steps
- Boundary analysis: workflow triggers on push vs. pull_request; required job timeouts
- Decision tables: mapping of missing artifacts -> blocking severity (P1 for missing CI that runs tests, P2 for missing optional docs)

Test cases (high level)
1) Existence: check for mandatory files (README.md, PULL_REQUEST_TEMPLATE.md, .github/workflows/ci.yml, docs/ONBOARDING.md)
2) CI content smoke: open ci.yml and assert strings indicating commands (pytest, flake8/ruff/black or eslint)
3) Workflow trigger: ensure workflows specify on: [push, pull_request] or at least pull_request
4) PR template: ensure checklist includes running tests and linking issue/epic
5) Onboarding completeness: docs/ONBOARDING.md contains 'run tests' and 'run linters' instructions

Automation and deliverables
- Automated pytest file: output/tests/test_repo_skeleton.py (this file will run the checks above)
- QA Report capturing pytest output and blocking items: output/reports/qa_repo_ci_report.md

Risk areas & recommended mitigations
- Risk: CI workflows use external actions that are private or deprecated -> Mitigation: prefer official actions and pin versions
- Risk: Workflows missing test step -> Mitigation: mark as P1 blocking for all downstream work

Next steps for Marcus
- Create the repo skeleton and CI artifacts as specified in Task 220
- Notify QA when done so automated tests can be re-run

QA owner
- Dana (QA) — will run the automated checks and sign-off when acceptance criteria are met
