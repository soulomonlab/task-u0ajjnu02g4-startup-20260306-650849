# Frontend CI Workflows — Samples

This file contains sample GitHub Actions workflow snippets to include in the repo skeleton for frontend runs. Each workflow assumes Node 18 and pnpm.

1) CI: lint, test, build (runs on pull_request to main)

name: Frontend CI
on:
  pull_request:
    branches: [ main ]

jobs:
  setup:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 18
          cache: 'pnpm'
      - name: Setup pnpm
        run: npm i -g pnpm@latest
      - name: Install Dependencies
        run: pnpm install --frozen-lockfile
      - name: Run Lint
        run: pnpm run lint
      - name: Run Tests
        run: pnpm run test:ci
      - name: Build
        run: pnpm run build


2) Storybook Preview (runs on push to main)

name: Storybook Deploy
on:
  push:
    branches: [ main ]

jobs:
  build-storybook:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 18
          cache: 'pnpm'
      - name: Setup pnpm
        run: npm i -g pnpm@latest
      - name: Install Dependencies
        run: pnpm install --frozen-lockfile
      - name: Build Storybook
        run: pnpm run build:storybook
      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: storybook-static
          path: storybook-static

3) E2E (Playwright) — runs nightly

name: Frontend E2E
on:
  schedule:
    - cron: '0 2 * * *'

jobs:
  e2e:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 18
          cache: 'pnpm'
      - name: Setup pnpm
        run: npm i -g pnpm@latest
      - name: Install Dependencies
        run: pnpm install --frozen-lockfile
      - name: Start App
        run: pnpm run start &
      - name: Run Playwright
        run: pnpm run test:e2e

Notes & decisions
- Use cache: 'pnpm' for setup-node to speed installs.
- Use --frozen-lockfile in CI for deterministic installs.
- Separate E2E job for resource isolation and to avoid PR slowness.

