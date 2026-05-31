# Repository instructions for GitHub Copilot

## Project context

This repository is a server-rendered Flask web application using Python 3.13, Jinja2 templates, HTML, CSS, JavaScript and Gunicorn for production serving.

## General behavior

- Prefer small, focused, reviewable changes.
- Follow the existing project structure and naming conventions.
- Do not introduce new frameworks, services, build tools or dependencies unless explicitly requested.
- Preserve existing public routes, template names, environment variables and deployment behavior unless the task explicitly asks to change them.
- Keep application logic out of templates.
- Keep route handlers thin and move non-trivial business logic into service/helper modules.
- Prefer maintainable, explicit code over clever abstractions.
- Do not hard-code secrets, credentials, tokens, private URLs or environment-specific values.
- Never expose stack traces, internal paths, secrets or raw exception details to end users.
- Use secure defaults for production code.
- When changing behavior, add or update tests if a test suite exists.
- When suggesting commands, prefer macOS/Linux shell syntax.
- Do not make broad unrelated rewrites.
- Explain required manual steps such as environment variables, migrations or deployment changes.