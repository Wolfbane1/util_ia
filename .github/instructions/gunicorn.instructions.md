---
applyTo: "{wsgi.py,gunicorn.conf.py,Procfile,*.service,deploy/**/*.sh,scripts/deploy*.sh}"
---

# Gunicorn and deployment instructions

- Use Gunicorn for production or production-like WSGI serving.
- Keep `wsgi.py` minimal.
- Do not put application business logic in `wsgi.py`.
- Gunicorn should target `wsgi:app` unless the project uses a different established entry point.
- Do not run Flask's development server in production.
- Do not enable Flask debug mode in production.
- Prefer environment variables for deployment configuration.
- Log to stdout/stderr in containerized or process-manager deployments.
- Avoid blindly increasing worker counts.
- Choose worker count based on deployment resources.
- Keep production commands explicit and reproducible.

- Recommended command:
```bash
gunicorn "wsgi:app"
```
- Typical production command:
```bash
gunicorn "wsgi:app" \
  --bind "0.0.0.0:8000" \
  --workers 3 \
  --timeout 60 \
  --access-logfile "-" \
  --error-logfile "-"
```
- Prefer a gunicorn.conf.py file for production configuration.
Example:
```python
bind = "0.0.0.0:8000"
workers = 3
timeout = 60
accesslog = "-"
errorlog = "-"
loglevel = "info"
``` 
- For worker count, use the deployment environment constraints. Do not blindly increase workers.
