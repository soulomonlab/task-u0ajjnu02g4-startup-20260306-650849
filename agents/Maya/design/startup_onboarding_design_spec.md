# Startup Project — Design & Onboarding Spec

Overview
- Purpose: Provide the design artifacts and onboarding checklist required for frontend and design work to begin in parallel with backend repo skeleton. This document scopes the initial design system, contributor UX, and wireframes for the MVP screens.
- Owner: Maya (UX/UI Designer)
- Intended recipients: Frontend (Kevin), Backend (Marcus), Product (Alex)

Summary of deliverables (in this file)
- Contributor onboarding checklist for designers & frontend
- Design repo layout and naming conventions
- Design system: tokens, core components, accessibility rules
- User flows & wireframes (ASCII) for primary screens
- Implementation notes & handoff requirements

1) Constraints & assumptions
- Backend API contracts will be defined by Marcus. Design should be loosely coupled and use feature flags/placeholders for API-driven content.
- Design assets hosted in Figma. Frontend should implement using tokens and Storybook components.
- Target breakpoints: desktop (>=1024px), tablet (768–1023px), mobile (<=767px).

2) Contributor onboarding checklist
- Designers:
  - Join Figma project: "SLACK_BOT / Startup Project"
  - Read this design spec and the product spec: output/specs/startup_project_spec.md
  - Create a component in the Design System page before building screens (name: ds/{component-name})
  - Export tokens file (JSON) via Figma tokens plugin to /design/tokens.json
- Frontend:
  - Create Storybook entry for each component before wiring screens
  - Implement tokens from /design/tokens.json
  - Use placeholder endpoints defined in API mock file until Marcus confirms real endpoints
- Cross-team:
  - Weekly sync cadence (initial week: daily stand-up) between Product, Design, Frontend, Backend
  - Record API contract needs in the shared API spec doc; tag Marcus when you need confirmation

3) Design repo layout (for designers & front-end asset organization)
- Figma structure (recommended):
  - File: Startup Project
    - Page: 00 - Cover + Readme (links to repo & specs)
    - Page: 01 - Design System
    - Page: 02 - Components
    - Page: 03 - Screens (labeled by route)
    - Page: 04 - Tokens & Export
- Git repo (frontend) suggested folders:
  - src/
    - design/tokens.json
    - components/
      - Button/
        - Button.tsx
        - Button.stories.tsx
        - Button.spec.tsx
        - Button.module.css
    - screens/
    - utils/
    - api/
  - .github/PULL_REQUEST_TEMPLATE.md
  - .github/workflows/storybook.yml

4) Design system — tokens
- Color (semantic):
  - color-bg-1: #FFFFFF (surface)
  - color-bg-2: #F7F8FA (elevated surface)
  - color-text-1: #0B1220 (primary text)
  - color-text-2: #6B7280 (secondary text)
  - color-action-primary: #2563EB (brand blue)
  - color-action-primary-hover: #1D4ED8
  - color-success: #16A34A
  - color-danger: #DC2626
- Typography:
  - font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial
  - type-xxl: 32px / 40px
  - type-xl: 24px / 32px
  - type-md: 16px / 24px
  - type-sm: 14px / 20px
- Spacing: base unit = 8px (multiples used: 8, 12, 16, 24, 32)
- Elevation: 0..3 with standardized shadows

Decision: semantic tokens (color-action-primary) used rather than raw hex across components to keep backend and feature toggles flexible.

5) Core components (priority for initial sprint)
- Button (primary, secondary, ghost) — props: size, disabled, loading, iconStart, iconEnd
- Input (text, password, textarea) — props: label, placeholder, error, helperText
- Card — use for lists/summary; supports actions and meta area
- TopNav / Header — includes app logo, primary nav, user avatar menu
- SideNav (desktop only) — collapsible
- Modal / Dialog — accessible focus trap
- Table / List item — for admin/management views

Component spec template (use in Storybook):
- Variants: normal, hover, active, disabled
- Accessibility: keyboard focus visible, aria-labels, contrast ratios >=4.5:1
- Tests: visual snapshots, keyboard navigation tests

6) User flows & wireframes (MVP screens)
- Primary user: Product manager / internal user who configures the bot and views reports

Flow 1: Onboard → Create Bot Instance
  1. Dashboard (list of bot instances) -> Create Bot (CTA)
  2. Create Bot modal / screen -> Name, Slack workspace, permissions -> Save
  3. Bot instance created -> Redirect to Instance Settings

ASCII wireframes (mobile / desktop simplified)

- Dashboard (desktop)
+----------------------------------------------------------+
| TopNav: [Logo] [Search]                 [Avatar]         |
+----------------------------------------------------------+
| SideNav |                Main area                          |
|         |  Header: My Bots              [Create Bot]        |
|         |  -----------------------------------------------  |
|         |  [Card] Bot A      [Card] Bot B      [Card] Bot C  |
|         |  (each card: status, last activity, quick actions) |
+----------------------------------------------------------+

- Create Bot modal
+-----------------------+
| Create Bot            |
| Name: [___________]   |
| Workspace: [Select]   |
| Permissions: [List]   |
| [Cancel]     [Create] |
+-----------------------+

Design note: Use cards for scannability and quick actions to reduce clicks.

7) Accessibility & internationalization
- All interactive elements must be keyboard reachable and have visible focus states
- Color contrast target: >=4.5:1 for normal text
- Use semantic HTML where possible; aria attributes for custom components
- Strings should be externalized for i18n (en/ko placeholders in Figma)

8) QA criteria for design acceptance
- Each component has Storybook entry demonstrating variants
- Visual regression baseline created (Chromatic or Storybook snapshots)
- Responsive behaviors verified at three breakpoints
- Accessibility audit (axe) passes critical checks

9) Implementation notes & dependencies
- Backend (Marcus): confirm API routes for bot creation, bot list, status fields. If API is delayed, frontend should consume mocked JSON under /api/mock/
- Frontend (Kevin): implement tokens.json and Storybook. Use CSS variables for theming to allow runtime overrides.
- Product (Alex): verify copy for CTAs and modal microcopy.

10) Next steps (by role)
- Designer (Maya): finalize Figma file and export tokens.json — DONE (in Figma)
- Backend (Marcus): provide API contract for bot endpoints (list, create, update, delete) — blocker until provided
- Frontend (Kevin): implement design system and components in Storybook; wire screens once API contracts confirmed

Document history
- v0.1 — initial draft — Maya

