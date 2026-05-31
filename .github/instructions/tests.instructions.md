---
applyTo: "tests/**/*.py"
---

# Test instructions

- Prefer pytest.
- Use Flask's test client for route tests.
- Test route status codes, redirects, validation errors and rendered behavior.
- Test service-layer logic separately from route handlers where practical.
- Avoid external network calls in tests.
- Mock external services.
- Keep tests deterministic.
- Use clear test names that describe expected behavior.
- Do not overfit tests to implementation details when behavior-level tests are sufficient.
