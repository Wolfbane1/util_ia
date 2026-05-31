---
applyTo: "app/templates/**/*.html"
---

# Jinja2 template instructions

- Use Jinja2 template inheritance.
- Prefer extending `base.html`.
- Keep templates focused on presentation.
- Avoid complex business logic in templates.
- Use macros or includes for repeated UI fragments.
- Use `url_for()` for links and static assets.
- Do not hard-code `/static/...` paths.
- Keep autoescaping enabled.
- Do not use `|safe` for user-generated content.
- Only use `|safe` for trusted, sanitized content.
- Use `tojson` when passing server data to JavaScript.
- Keep indentation consistent.
- Prefer semantic and accessible HTML.
- Use visible validation messages for forms.

- Prefer a shared base template:
```html
<!-- templates/base.html -->
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{% block title %}Application{% endblock %}</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
</head>
<body>
  <header>
    {% block header %}{% endblock %}
  </header>
  <main>
    {% block content %}{% endblock %}
  </main>
  <script src="{{ url_for('static', filename='js/main.js') }}" defer></script>
  {% block scripts %}{% endblock %}
</body>
</html>
```
- Child templates should extend base.html:
```html
{% extends "base.html" %}
{% block title %}Home{% endblock %}
{% block content %}
  <h1>Hello</h1>
{% endblock %}
```
- Template rules:
* Keep templates focused on presentation.
* Avoid complex business logic in templates.
* Use macros for repeated UI fragments.
* Use includes for reusable sections.
* Use url_for() for static files and links.
* Do not hard-code static asset paths.
* Do not duplicate large blocks of HTML across templates.
* Keep indentation consistent.
* Prefer semantic HTML.

- Avoid:
```html
<link rel="stylesheet" href="/static/css/main.css">
```

- Prefer:
```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
```
