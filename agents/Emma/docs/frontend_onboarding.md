# Frontend Onboarding (Developer-facing)

Overview
- Purpose: Fast, repeatable onboarding for frontend engineers so they can start implementing UI features against the repository skeleton and CI workflows.
- Audience: Frontend engineers, contractors, and new hires.

Quickstart (get up & running in < 5 minutes)
1. Clone repo:
   git clone git@github.com:your-org/your-repo.git
2. Install dependencies (pnpm recommended):
   pnpm install
3. Start dev server:
   pnpm dev
4. Run tests:
   pnpm test

Repository layout (expected for frontend package)
- /packages/frontend/  -> source code (React/Next/Vue as chosen)
- /packages/ui/        -> shared UI components
- /packages/utils/     -> shared utilities
- /apps/               -> optional app-level entries for monorepo
- /package.json        -> workspace configuration (if monorepo)
- /.github/workflows/  -> CI workflows (see CI quick reference)
- /.env.example        -> example environment variables for developers

Monorepo vs single-package
- Recommendation: Use a monorepo when frontend shares components, types, or tooling across multiple packages/apps. pnpm workspaces scale well and are faster than npm/yarn in CI caching.
- Decision owner: Backend/Repo owner (Marcus) — confirm whether to use monorepo before creating package manifests.

Package manager
- Recommendation: pnpm (faster installs, deterministic node_modules layout, good workspace support).
- Fallback: yarn v1 or npm if pnpm is not an option.

Environment
- Add a top-level /.env.example containing keys required to run locally (API_BASE_URL, NEXT_PUBLIC_..., FEATURE_FLAGS).
- Do NOT commit secrets. Use GitHub Actions secrets for CI.

Local developer checks
- Pre-commit: lint-staged + eslint + prettier
- Pre-push (optional): run unit tests

CI & branching
- Workflows go under: .github/workflows/
- Branch strategy: feature/* for features, fix/* for bugfixes, release/* for releases
- PR template: standardize title, summary, testing steps, and checklist (see PR template file)

Where to find more
- CI quick reference: output/docs/frontend_ci_quickreference.md
- PR template: output/docs/frontend_pr_template.md

Notes & outstanding decisions
- Marcus to confirm: monorepo vs single-package; package manager enforcement; location of example env file.
- If monorepo accepted, frontend package paths above should be adjusted to match repository convention.
