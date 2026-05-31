---
applyTo: "**/*.py"
---

# Python 3.13 instructions

- Target Python 3.13.
- Use modern Python type hints: `str | None`, `list[str]`, `dict[str, Any]`.
- Prefer `pathlib.Path` over manual path string manipulation.
- Prefer `datetime.UTC` and timezone-aware datetimes.
- Use `zoneinfo` instead of `pytz`.
- `match` statements only when they improve clarity.
- Use f-strings for interpolation.
- Keep functions small and focused.
- Use explicit error handling.
- Do not catch broad exceptions unless there is a clear recovery or logging strategy.
- Use `logging`, not `print()`, for application logs.
- Do not log secrets, tokens, passwords, cookies or authorization headers.
- Keep imports grouped as standard library, third-party and local.
- Write Black-compatible formatting.
- Use docstrings when they clarify public functions, complex behavior or service boundaries.
- Avoid deprecated APIs and compatibility code for unsupported Python versions.

## Python style
Follow:
- PEP 8 
- PEP 257 for docstrings where docstrings are useful
- Clear function boundaries
- Explicit error handling
- Small functions with focused responsibility
- Every class has a variable called _class_name with the name of the class.
- Every method has a variable called method with the name of the method. 

- Prefer:
```python
from pathlib import Path
from typing import Any
BASE_DIR = Path(__file__).resolve().parent
```
- Avoid:
```python
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
```
- Use type hints like:
```python
def get_user(user_id: int) -> User | None:
    ...
```

- For dictionaries with flexible data, prefer:
```python
def process_data(data: dict[str, Any]) -> None:
    ...
```

## Logging 
- Use Python’s logging module.
- Do not use print() for application logging.
- Example:
```python
import logging
logger = logging.getLogger(__name__)
logger.info("User profile updated", extra={"user_id": user_id})
```
- Do not log secrets or sensitive data.
- Use always the _class_name and method variables in log messages for better traceability.     
```python
logger.info(f"{self._class_name}.{method}: User profile updated", extra={"user_id": user_id})
``` 
- Every method has a first logging with the -START after the method in debug mode. 
```python
logger.info(f"{self._class_name}.{method}-START: User profile updated", extra={"user_id": user_id})
``` 
- Every method has a last logging with the -END after the method in debug mode. 
```python
logger.info(f"{self._class_name}.{method}-END: User profile updated", extra={"user_id": user_id})
``` 