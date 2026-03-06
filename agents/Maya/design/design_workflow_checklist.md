# Design Workflow & Handoff Checklist

Purpose: Standardize how design work is delivered to frontend to avoid rework and ensure implementability.

Owner: Maya (Designer)

Checklist
- [ ] Storybook stories created for each component before screen wiring
- [ ] Tokens exported (design/tokens.json) and added to repo
- [ ] Component spec sheet completed (props, states, accessibility)
- [ ] Responsive behavior documented (breakpoints & layout adjustments)
- [ ] Figma prototypes for critical flows (Create Bot, Auth)
- [ ] Acceptance criteria listed in Storybook stories
- [ ] Visual regression baseline recorded

Naming conventions
- Components: PascalCase (Button, TopNav)
- Tokens: semantic names (color-action-primary)

Notes
- Use comments in Figma to explain non-obvious interaction
- When API fields are uncertain, use prefixed mock keys: _mock_bot_id

