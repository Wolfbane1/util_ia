---
applyTo: "app/static/**/*.js"
---

# JavaScript instructions

- Use JavaScript for progressive enhancement.
- Keep core server-rendered flows usable without JavaScript where reasonable.
- Use modern browser APIs.
- Use `const` and `let`, not `var`.
- Avoid heavy frontend dependencies unless already present.
- Do not introduce frontend frameworks unless explicitly requested.
- Keep scripts in `app/static/js/`.
- Avoid large inline scripts in templates.
- When consuming server-rendered data, expect it to be emitted through Jinja2 `tojson`.
- Validate assumptions about DOM elements before using them.
- Avoid global variables unless the existing project uses them intentionally.
- Use defer for scripts:
```html
<script src="{{ url_for('static', filename='js/main.js') }}" defer></script>
```
- Do not put large scripts inline inside templates unless there is a specific reason.
- When passing server data to JavaScript, use JSON safely:
```html
<script>
  const config = {{ config_data | tojson }};
</script>
```
- Do not manually interpolate unescaped values into JavaScript.