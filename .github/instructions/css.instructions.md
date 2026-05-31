---
applyTo: "app/static/**/*.css"
---

# CSS instructions

- Use project-local CSS unless a CSS framework already exists.
- Do not introduce Tailwind, Bootstrap, Sass, PostCSS or other tooling unless explicitly requested.
- Avoid inline styles.
- Use clear, stable class names.
- Prefer responsive layouts.
- Keep selectors simple and maintainable.
- Preserve existing naming conventions.
- Group related rules together.
- Ensure visible focus states for interactive elements.
- Do not rely only on color for meaning.
- Prefer project-local CSS unless the project already uses a CSS framework.
- Keep CSS organized by component or page.
- Avoid excessive inline styles.
- Use clear class names:
```html
<div class="user-card">
```
- Prefer responsive layouts.
- Do not introduce Tailwind, Bootstrap, Bulma, Sass, PostCSS, or build tooling unless already present or explicitly requested.
