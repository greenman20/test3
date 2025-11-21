## Hello Script Documentation

### Overview
- `Hello.py` is a minimal entry-point script that demonstrates sending text output to stdout.
- The script executes immediately when invoked and prints a single greeting (`"Hello, World!"`).

### Public API
- **Module:** `Hello.py`
  - **Behavior:** Runs a top-level statement `print("Hello, World!")` as soon as the module is executed.
  - **Purpose:** Provide a canonical example or quick smoke-test for the runtime environment.

### Usage
- **From the command line**
  - Ensure Python 3.x is installed.
  - Run `python Hello.py` from the repository root.
  - Expected output:

```
Hello, World!
```

### Integration Examples
- **As a script entry point**
  - Add the module to tooling or CI checks to validate that Python is configured correctly.
- **As an importable module**
  - Importing `Hello` will execute the `print` statement once; avoid importing it in library code unless you want the side effect.

### Extensibility Notes
- Wrap the greeting in a function (e.g., `def say_hello():`) if you need reusable logic.
- Parameterize the greeting message via function arguments or environment variables for different locales or contexts.

### Testing Guidance
- Run the script manually and assert that stdout contains the expected greeting.
- For automated tests, capture stdout (e.g., with `capsys` in pytest) and compare against `"Hello, World!\n"`.
