# GitHub Copilot Instructions
# Type Hints and Static Analysis
- All generated Python code must include full type hints.
- Add type annotations to:
  - Function arguments
  - Return values
  - Class attributes
  - Local variables (where appropriate)
- Do not generate code that causes errors in mypy.
- Avoid `Any` unless it is explicitly required.
- Prefer precise types (e.g., `list[str]` over `List[Any]`).

# Flake8 Compliance
- All generated code must fully comply with flake8 rules.
- Avoid unused variables, unused imports, and long lines.
- Follow PEP8 for formatting and naming conventions.