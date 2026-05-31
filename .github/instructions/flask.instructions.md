---
applyTo: "app/**/*.py"
---

# Flask instructions

- Treat the project as a server-rendered Flask application.
- Prefer the application factory pattern if the project already uses it.
- Use Blueprints for route organization.
- Keep route handlers thin.
- Move non-trivial business logic into service modules.
- Use `render_template()` for HTML pages.
- Do not use `render_template_string()` for normal pages.
- Use `url_for()` instead of hard-coded internal URLs.
- Use `redirect()` after successful POST requests.
- Validate all form, query-string and JSON input.
- Return appropriate HTTP status codes.
- Do not leak internal exception details to users.
- Use Flask error handlers for user-facing error pages where appropriate.
- Keep configuration environment-driven.
- Do not enable Flask debug mode in production.
- Do not store secrets in source code.
- Use secure cookie settings in production:
  - `SESSION_COOKIE_HTTPONLY = True`
  - `SESSION_COOKIE_SECURE = True`
  - `SESSION_COOKIE_SAMESITE = "Lax"`

## Flask Architecture & Best Practices
- Prefer the application factory pattern unless the current project uses a different established pattern.
- Recommended structure:
```project/
├── app/
│   ├── __init__.py  # create_app function
│   ├── routes/
│   │   ├── __init__.py  # Blueprint registrations
│   │   ├── main.py  # main blueprint
│   │   ├── auth.py  # auth blueprint
│   ├── models.py  # database models
│   ├── extensions.py  # db, mail, etc. initialization 
├── templates/
├── static/
├── config.py  # configuration classes
├── gunicorn_config.py  # Gunicorn configuration
├── requirements.txt
```

- Prefer this pattern:
```python
from flask import Flask

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("app.config.Config")
    register_blueprints(app)
    register_error_handlers(app)

    return app
```

- Use wsgi.py as the production entry point:
```python
from app import create_app  
app = create_app()
``` 

- Gunicorn should target:
```bash
gunicorn wsgi:app
```
- Do not put substantial application logic inside wsgi.py. 

- **Extensions**: Initialize extensions using `init_app` pattern to avoid circular imports and support app factories.
- **Blueprints**: Organize large applications into Blueprints by feature (e.g., auth, users, api). Keep blueprints focused and avoid deep nesting.
- **Error Handling**: Implement global error handlers for common errors (404, 500) that return appropriate JSON or HTML responses.>>>

## Flask Routes
When adding routes:
- Use Blueprints for route organization.
- Keep route functions thin.
- Move business logic into service modules.
- Validate and sanitize user input.
- Return appropriate HTTP status codes.
- Use url_for() instead of hard-coded URLs.
- Use redirect() after successful POST requests to avoid duplicate form submissions.
- Keep HTML rendering in templates, not string literals inside Python code.
- Example:
```python
from flask import Blueprint, render_template, request, redirect, url_for, flash

bp = Blueprint("main", __name__)
@bp.get("/")
def index():
    return render_template("index.html")

@bp.post("/contact")
def contact_submit():
    name = request.form.get("name", "").strip()
    if not name:
        flash("Name is required.", "error")
        return redirect(url_for("main.index"))
    return redirect(url_for("main.thank_you"))
```
- Prefer explicit methods:
```python
@bp.get("/items")
@bp.post("/items")
```
Over:
```python 
@bp.route("/items", methods=["GET", "POST"])
```
