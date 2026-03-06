# Frontend CI Quick Reference

Purpose
- Provide frontend engineers and Marcus (repo owner) with a concise CI workflow checklist and examples to be placed under .github/workflows.

Key CI jobs for frontend
1. install-deps
   - Use pnpm install --frozen-lockfile
   - Cache pnpm store and node_modules for speed
2. lint
   - Run eslint --ext .js,.jsx,.ts,.tsx
3. test
   - Run unit tests (pnpm test) with coverage
   - Upload coverage as artifact if needed
4. build
   - Run production build (pnpm build)
5. deploy-preview (optional)
   - Trigger preview deploy to Vercel/Netlify on PR

Sample workflow placement and naming conventions
- .github/workflows/frontend-ci.yml
- .github/workflows/frontend-pr-preview.yml (optional)

Caching recommendations
- Use actions/cache for pnpm store and .pnpm-store
- Key collision strategy: node-version + hash(package-lock.json or pnpm-lock.yaml)

Secrets & environment in CI
- Store API keys and tokens in GitHub Secrets
- Use env: variables only for non-secret values

Runners
- Use ubuntu-latest for Node-based builds
- Consider macOS runners only if iOS simulator jobs are required

Matrix builds
- If supporting multiple node versions: use strategy.matrix.node-version
- Include browser matrix if running E2E tests against multiple browsers

Artifacts
- Persist build artifacts and coverage reports for debugging

Failure handling
- Set 'continue-on-error: false' for test and lint job to fail fast
- Add retry logic for flaky network steps (checkout, cache restore)

Links
- pnpm CI docs: https://pnpm.io/ci
- GitHub Actions cache docs: https://docs.github.com/actions/advanced-guides/caching-dependencies-and-builds

Outstanding decisions for Marcus
- Confirm pnpm vs other package manager
- Approve caching strategy and runner selection

Where to find more
- Frontend onboarding: output/docs/frontend_onboarding.md
- PR template: output/docs/frontend_pr_template.md
