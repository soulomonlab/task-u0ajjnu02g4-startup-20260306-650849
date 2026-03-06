# Auth Flow Wireframes & Component Specs

Purpose: Provide wireframes and component interaction details for user authentication flows (Login, Signup, Forgot Password). Needed early so frontend can scaffold auth routes and UI before backend endpoints are finalized.

Owner: Maya (UX/UI Designer)

1) User scenarios
- Internal PM logs in to manage bots
- New user invited to the platform accepts and sets a password
- User forgets password and resets via email

2) Screens & brief behavior
- Login screen
  - Email
  - Password
  - Remember me (optional)
  - CTA: Sign in
  - Links: Forgot password, Sign up
- Signup screen (invite link or open signup)
  - Name, Email, Password
  - CTA: Create account
- Forgot Password
  - Enter email -> Email sent confirmation

3) Wireframes (ASCII)

- Login (mobile)
+---------------------------+
| Logo                      |
| Email [________________]  |
| Password [______________] |
| [ ] Remember me  [Sign in] |
| Forgot password? Sign up   |
+---------------------------+

- Signup (desktop)
+----------------------------------+
| Left: illustration               |  Right: Form                      |
|                                  |  Name: [______]                   |
|                                  |  Email: [______]                  |
|                                  |  Password: [______]               |
|                                  |  [Create account]                 |
+----------------------------------+

4) Component interactions
- Password field: toggle show/hide, strength meter after 3+ chars
- Submit buttons: show loading spinner, disabled state on invalid form
- Error handling: inline errors under fields, global error toast for server errors

5) Accessibility
- Labels associated with inputs, error messages linked with aria-describedby
- Keyboard-first: tab order logical, enter submits

6) Handoff requirements for Frontend
- Tokens for spacing and colors (see design spec)
- Copy for links and error messages (Alex to confirm)
- Mock endpoints for auth flows until Marcus provides real APIs

