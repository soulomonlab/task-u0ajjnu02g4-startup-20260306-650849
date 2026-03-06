# Repo skeleton & CI checklist

Purpose
- Provide a single, opinionated repository layout and CI checklist so all streams can onboard quickly and work in a consistent, maintainable way.

Scope
- Backend (Python/FastAPI), Frontend (React), Infra (deployment manifests), DevOps (CI/CD), Tests, Docs.

Repository layout (recommended)

- .github/
  - workflows/        # CI/CD workflows (GitHub Actions YAMLs)
- infra/              # Terraform / k8s manifests / helm charts
- services/
  - backend/          # Python FastAPI service
    - app/
      - api/
      - core/
      - db/
      - tasks/
    - tests/
    - Dockerfile
    - pyproject.toml
  - frontend/         # React app
    - src/
    - public/
    - tests/
    - Dockerfile
- scripts/            # helper scripts (local dev, migrations)
- docs/               # user & dev docs (architecture, runbooks)
- specs/              # product & design specs (PRDs)
- config/             # CI templates, PR templates, coding standards
- .env.example        # example env vars
- README.md
- CODEOWNERS
- CONTRIBUTING.md

Branching and release strategy
- Main branch: main (always deployable)
- Feature branches: feat/<short-desc>-<issue#>
- Bugfix branches: fix/<short-desc>-<issue#>
- Hotfix branches: hotfix/<version>
- Release flow: create release branch release/x.y -> merge to main -> tag
- Protect main: require PR, 1+ approvals, green CI, signed commits optional

Directory responsibilities (short)
- services/backend: authoritative backend code, API definitions, DB migrations
- services/frontend: React SPA and static assets
- infra: infra-as-code and deployment manifests, owned by DevOps
- scripts: dev utilities (db reset, local debug server)
- docs: living architecture and runbooks

Coding & quality conventions
- Python: pyproject.toml (poetry or pip-tools); ruff for linting; pytest for tests
- JS/TS: ESLint + Prettier; unit + e2e tests (Jest + Playwright or Cypress)
- Formatting: enforce via pre-commit hooks
- Type checking: mypy for Python, TypeScript compiler for frontend
- Tests: aim for >80% coverage on backend critical modules

CI checklist (minimal required for PRs)
1. Lint: ruff (Python) / ESLint (frontend)
2. Type checks: mypy (Python) / tsc (frontend)
3. Unit tests: pytest / jest (fail on < threshold)
4. Security scan: Snyk/Dependabot alerts or GitHub code scanning
5. Build: build Docker image for the affected service
6. Integration smoke tests: optional, run on PR merge to release branch
7. Artifacts: publish test coverage and built image to registry
8. PR metadata: linked issue, description, screenshots if UI change

PR requirements
- Small, focused PRs. Reference issue number. Provide runbook if applicable.
- PR template (see config/PULL_REQUEST_TEMPLATE.md)
- Include `Risk: low/med/high` and `Rollback` plan

Onboarding checklist for new contributors
- Install dev tooling (VSCode+extensions, python, node, Docker)
- Copy .env.example to .env and set local DB credentials
- Run scripts/dev_setup.sh (creates virtualenv, installs deps)
- Run linters and unit tests locally
- Read CONTRIBUTING.md and CODEOWNERS

Observability & tracing
- All services must include OpenTelemetry initialization and export to OTLP
- Instrument key endpoints and DB queries (p95 budget: <100ms)

Decisions made
- Monorepo layout under services/ to simplify cross-service changes
- GitHub Actions as primary CI for simplicity and transparency
- Enforced code quality gates on PRs

Risks & mitigations
- Large monorepo may slow CI: mitigate with path filters and test matrix sharding
- Missing infra ownership: require DevOps (Noah) to own infra/ folder

References
- PR template: config/PULL_REQUEST_TEMPLATE.md
- Sample workflows: config/.github_workflows/ci.yml, config/.github_workflows/pr_checks.yml
