# Frontend Repo Layout — Proposal

Purpose
- Provide a ready-to-use frontend repo layout and conventions so frontend work can begin immediately and integrate smoothly into the overall repo skeleton and CI.

High-level decisions (reversible)
- Tooling: React 18 + TypeScript + Vite — fast DX, small bundle.
- Styling: Tailwind CSS utility-first (already in team stack).
- Package manager: pnpm (performance + monorepo friendliness). Can be switched to npm/yarn if needed.
- State: Zustand for global state; React Query reserved for server-cached data (decide per feature).
- Testing: React Testing Library + Vitest for unit; Cypress/Playwright for E2E (separate CI job).
- Storybook for isolated component dev + visual review.

Repository layout (single-package frontend)

/ (repo root)
- apps/frontend/             # frontend app (Vite + TS)
  - .github/                # CI workflows (can be at root too)
  - public/
  - src/
    - main.tsx
    - App.tsx
    - index.css
    - assets/
    - features/             # feature folders (domain-driven)
      - auth/
        - components/
        - hooks/
        - types.ts
        - auth.slice.ts
    - components/           # shared, presentational components
      - Button/
        - Button.tsx
        - Button.test.tsx
        - Button.stories.tsx
    - lib/                  # utilities, api client, formatters
      - api.ts
      - fetcher.ts
    - stores/                # Zustand stores
    - routes/
    - hooks/
    - styles/
    - types/
  - tests/                  # e2e test entrypoints (if colocated)
  - vitest.config.ts
  - vite.config.ts
  - package.json
  - tsconfig.json
  - tailwind.config.js
  - .eslintrc.cjs
  - .prettierrc
  - README.md

If monorepo is preferred (recommended for backend/frontend/apps/libs):
- apps/frontend/
- apps/backend/
- packages/ui/              # shared UI library (storybook)
- packages/tsconfig/
- package.json (root: tooling scripts)
- pnpm-workspace.yaml

Scripts (package.json) — essential
- dev: vite
- build: vite build
- preview: vite preview
- lint: eslint "src/**"
- format: prettier --write "src/**"
- test: vitest
- test:ci: vitest --run
- storybook: storybook dev
- build:storybook: storybook build

Recommended conventions
- Feature folders (co-locate components, hooks, tests).
- Prefer small, focused components + composition.
- Types: explicit exported types in src/types per feature.
- Accessibility: add axe or jest-axe to tests for critical components.
- Commit messages: Conventional Commits (helps changelog + release automation).

Environments & Secrets
- Use VITE_ prefix for client env vars (Vite requirement).
- Provide .env.example in repo root with required keys.

Hand-off artifacts included (in this PR)
- frontend_repo_layout.md (this file)
- frontend_ci_workflows.md (sample workflows)
- frontend_pr_template.md (PR template for frontend work)

Open questions / assumptions for Marcus
1. Are we adopting monorepo at repo level? I assumed yes but single-package is OK too.
2. Preferred package manager? I recommended pnpm.
3. CI runner constraints (self-hosted vs GitHub-hosted) — affects caching strategy.

Why this matters
- Removes ambiguity for frontend devs starting work.
- Gives Marcus concrete artifacts to include into the global repo skeleton & CI checklist.

