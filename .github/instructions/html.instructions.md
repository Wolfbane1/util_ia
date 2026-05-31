---
applyTo: "**/*.html"
---

# HTML instructions

- Write semantic HTML.
- Use proper heading hierarchy.
- Use `<main>`, `<header>`, `<nav>`, `<section>`, `<article>` and `<footer>` where appropriate.
- Use labels for all form controls.
- Use buttons for actions and links for navigation.
- Provide useful `alt` text for meaningful images.
- Avoid clickable `<div>` or `<span>` elements.
- Prefer progressive enhancement: core flows should work without JavaScript where reasonable.
- Do not rely only on color to convey meaning.
- Keep markup readable and consistently indented.
- Forms should include labels:
```html
<label for="email">Email</label>
<input id="email" name="email" type="email" required>
```
- Avoid inaccessible markup such as clickable <div> elements.
- Use progressive enhancement: server-rendered pages should remain usable without JavaScript for core flows whenever reasonable.