# Hello World Module

A comprehensive, well-documented Python module demonstrating greeting functionality with best practices for code documentation and API design.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [API Reference](#api-reference)
  - [Functions](#functions)
  - [Constants](#constants)
- [Usage Examples](#usage-examples)
- [Development](#development)
- [Testing](#testing)
- [Contributing](#contributing)

## Overview

The Hello module provides a simple yet extensible API for generating and displaying greeting messages. It demonstrates:

- ✨ Clean, documented Python code
- 📝 Comprehensive docstrings following Google/NumPy style
- 🔧 Flexible API with sensible defaults
- 🧪 Testable, pure functions
- 📦 Module and script dual-purpose design

## Installation

No external dependencies required! This module uses only Python standard library.

### Requirements

- Python 3.6 or higher

### Setup

1. Clone or download the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. The module is ready to use immediately:
```bash
python Hello.py
```

## Quick Start

### As a Script

Run directly from the command line:

```bash
python Hello.py
```

Output:
```
Hello, World!
```

### As a Module

Import and use in your Python code:

```python
from Hello import greet, greet_person, print_greet

# Generate greeting strings
message = greet()                          # "Hello, World!"
custom = greet("Hi", "Python")             # "Hi, Python!"

# Greet specific people
person = greet_person("Alice")             # "Hello, Alice!"
friendly = greet_person("Bob", "Hey")      # "Hey, Bob!"

# Print directly to stdout
print_greet()                              # Prints: Hello, World!
print_greet("Good morning", "Team")        # Prints: Good morning, Team!
```

## API Reference

### Functions

#### `greet(greeting=DEFAULT_GREETING, target="World")`

Generate a greeting message string.

**Parameters:**
- `greeting` (str, optional): The greeting phrase. Default: `"Hello"`
- `target` (str, optional): The recipient of the greeting. Default: `"World"`

**Returns:**
- `str`: A formatted greeting message

**Examples:**

```python
>>> from Hello import greet
>>> greet()
'Hello, World!'
>>> greet("Hi")
'Hi, World!'
>>> greet("Good evening", "everyone")
'Good evening, everyone!'
>>> greet(target="Developer")
'Hello, Developer!'
```

**Use Cases:**
- Generating welcome messages for applications
- Creating personalized notifications
- Template-based message generation
- Internationalization string building

---

#### `greet_person(name, greeting=DEFAULT_GREETING)`

Generate a personalized greeting for a specific person.

**Parameters:**
- `name` (str, **required**): The name of the person to greet
- `greeting` (str, optional): The greeting phrase. Default: `"Hello"`

**Returns:**
- `str`: A personalized greeting message

**Raises:**
- `ValueError`: If name is empty or contains only whitespace

**Examples:**

```python
>>> from Hello import greet_person
>>> greet_person("Alice")
'Hello, Alice!'
>>> greet_person("Bob", "Welcome")
'Welcome, Bob!'
>>> greet_person("Charlie", greeting="Hi")
'Hi, Charlie!'

# Error handling
>>> greet_person("")
ValueError: Name cannot be empty or whitespace only
>>> greet_person("   ")
ValueError: Name cannot be empty or whitespace only
```

**Use Cases:**
- User onboarding flows
- Personalized email generation
- Chat bot responses
- Welcome screens

---

#### `print_greet(greeting=DEFAULT_GREETING, target="World")`

Print a greeting message directly to stdout.

**Parameters:**
- `greeting` (str, optional): The greeting phrase. Default: `"Hello"`
- `target` (str, optional): The recipient of the greeting. Default: `"World"`

**Returns:**
- `None`: Prints to stdout but returns nothing

**Examples:**

```python
>>> from Hello import print_greet
>>> print_greet()
Hello, World!
>>> print_greet("Hi", "there")
Hi, there!
>>> print_greet(greeting="Welcome", target="home")
Welcome, home!
```

**Use Cases:**
- Command-line applications
- Quick debugging output
- Console-based user interfaces
- Script execution feedback

**Note:** This function has side effects. For more testable code, prefer using `greet()` and handling output separately.

---

#### `main()`

Main entry point when the module is executed as a script.

**Parameters:**
- None

**Returns:**
- `None`: Exits with status 0 on success

**Examples:**

```bash
$ python Hello.py
Hello, World!
```

**Note:** This function only executes when running the module directly, not when importing it.

---

### Constants

#### `DEFAULT_GREETING`

The default greeting phrase used throughout the module.

**Type:** `str`  
**Value:** `"Hello"`

**Usage:**

```python
from Hello import DEFAULT_GREETING, greet

# Use the default
print(DEFAULT_GREETING)  # "Hello"

# Override in function calls
greet(greeting="Hi")  # Uses custom greeting
greet()               # Uses DEFAULT_GREETING
```

## Usage Examples

### Example 1: Simple CLI Tool

```python
#!/usr/bin/env python3
from Hello import greet_person
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = " ".join(sys.argv[1:])
        print(greet_person(name))
    else:
        print("Usage: python script.py <name>")
```

Run it:
```bash
$ python script.py Alice
Hello, Alice!
```

### Example 2: Web Application Integration

```python
from flask import Flask, request
from Hello import greet, greet_person

app = Flask(__name__)

@app.route('/greet')
def greet_endpoint():
    name = request.args.get('name', 'World')
    greeting = request.args.get('greeting', 'Hello')
    
    if name == 'World':
        return greet(greeting, name)
    else:
        return greet_person(name, greeting)

if __name__ == '__main__':
    app.run()
```

### Example 3: Batch Greeting Generator

```python
from Hello import greet_person

def greet_team(team_members, greeting="Hello"):
    """Generate greetings for a list of team members."""
    greetings = []
    for member in team_members:
        try:
            greetings.append(greet_person(member, greeting))
        except ValueError as e:
            print(f"Warning: Skipping invalid name - {e}")
    return greetings

# Usage
team = ["Alice", "Bob", "Charlie", "", "Diana"]
messages = greet_team(team, "Welcome")
for msg in messages:
    print(msg)
```

Output:
```
Warning: Skipping invalid name - Name cannot be empty or whitespace only
Welcome, Alice!
Welcome, Bob!
Welcome, Charlie!
Welcome, Diana!
```

### Example 4: Internationalization

```python
from Hello import greet

# Define greetings in different languages
GREETINGS = {
    'en': 'Hello',
    'es': 'Hola',
    'fr': 'Bonjour',
    'de': 'Guten Tag',
    'it': 'Ciao',
    'ja': 'こんにちは',
}

def international_greet(name, language='en'):
    """Greet someone in their preferred language."""
    greeting = GREETINGS.get(language, GREETINGS['en'])
    return greet(greeting, name)

# Usage
print(international_greet("World", "es"))  # Hola, World!
print(international_greet("World", "fr"))  # Bonjour, World!
print(international_greet("World", "ja"))  # こんにちは, World!
```

### Example 5: Error Handling

```python
from Hello import greet_person

def safe_greet(name, greeting="Hello", fallback="Guest"):
    """
    Safely greet a user with fallback for invalid names.
    """
    try:
        return greet_person(name, greeting)
    except ValueError:
        # Use fallback name if provided name is invalid
        return greet_person(fallback, greeting)

# Usage
print(safe_greet("Alice"))        # Hello, Alice!
print(safe_greet(""))            # Hello, Guest!
print(safe_greet("   "))         # Hello, Guest!
print(safe_greet("", fallback="Friend"))  # Hello, Friend!
```

## Development

### Project Structure

```
.
├── Hello.py          # Main module with all functionality
└── README.md         # This documentation file
```

### Code Style

This project follows PEP 8 Python style guidelines:
- Maximum line length: 79 characters for code, 72 for docstrings
- Google/NumPy style docstrings
- Type hints where appropriate
- Comprehensive documentation for all public APIs

### Running the Module

**As a script:**
```bash
python Hello.py
```

**In Python interpreter:**
```python
>>> import Hello
>>> Hello.greet()
'Hello, World!'
```

**With python -m:**
```bash
python -m Hello  # If configured as a package
```

## Testing

### Manual Testing

Test the functions interactively in Python:

```python
>>> from Hello import greet, greet_person, print_greet
>>> 
>>> # Test basic functionality
>>> assert greet() == "Hello, World!"
>>> assert greet("Hi") == "Hi, World!"
>>> assert greet("Hey", "Python") == "Hey, Python!"
>>> 
>>> # Test person greeting
>>> assert greet_person("Alice") == "Hello, Alice!"
>>> assert greet_person("Bob", "Hi") == "Hi, Bob!"
>>> 
>>> # Test error handling
>>> try:
...     greet_person("")
...     assert False, "Should raise ValueError"
... except ValueError:
...     pass  # Expected
>>> 
>>> print("All tests passed!")
```

### Automated Testing with unittest

Create a test file `test_hello.py`:

```python
import unittest
from Hello import greet, greet_person, print_greet, DEFAULT_GREETING

class TestHelloModule(unittest.TestCase):
    
    def test_greet_default(self):
        """Test greet with default parameters."""
        self.assertEqual(greet(), "Hello, World!")
    
    def test_greet_custom_greeting(self):
        """Test greet with custom greeting."""
        self.assertEqual(greet("Hi"), "Hi, World!")
    
    def test_greet_custom_target(self):
        """Test greet with custom target."""
        self.assertEqual(greet(target="Python"), "Hello, Python!")
    
    def test_greet_both_custom(self):
        """Test greet with both parameters custom."""
        self.assertEqual(greet("Hey", "there"), "Hey, there!")
    
    def test_greet_person_valid(self):
        """Test greet_person with valid name."""
        self.assertEqual(greet_person("Alice"), "Hello, Alice!")
    
    def test_greet_person_custom_greeting(self):
        """Test greet_person with custom greeting."""
        self.assertEqual(greet_person("Bob", "Hi"), "Hi, Bob!")
    
    def test_greet_person_empty_name(self):
        """Test greet_person raises ValueError for empty name."""
        with self.assertRaises(ValueError):
            greet_person("")
    
    def test_greet_person_whitespace_name(self):
        """Test greet_person raises ValueError for whitespace-only name."""
        with self.assertRaises(ValueError):
            greet_person("   ")
    
    def test_default_greeting_constant(self):
        """Test DEFAULT_GREETING constant value."""
        self.assertEqual(DEFAULT_GREETING, "Hello")

if __name__ == '__main__':
    unittest.main()
```

Run tests:
```bash
python -m unittest test_hello.py -v
```

### Automated Testing with pytest

If you have pytest installed:

```bash
pip install pytest
pytest test_hello.py -v
```

### Doctests

The module includes doctests in docstrings. Run them with:

```bash
python -m doctest Hello.py -v
```

## Contributing

Contributions are welcome! Here's how you can help:

1. **Report Bugs**: Open an issue describing the bug and how to reproduce it
2. **Suggest Features**: Open an issue describing the feature and its use case
3. **Submit Pull Requests**: 
   - Fork the repository
   - Create a feature branch
   - Add tests for new functionality
   - Ensure all tests pass
   - Update documentation
   - Submit a pull request

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Add comprehensive docstrings for new functions
- Include usage examples in docstrings
- Add unit tests for new functionality
- Update README.md with new features
- Keep functions pure where possible (minimize side effects)

## License

This project is provided as-is for educational and demonstration purposes.

---

## Support

For questions, issues, or suggestions, please open an issue in the repository.

## Changelog

### Version 1.0.0 (Initial Release)
- Initial implementation with basic greeting functionality
- Comprehensive documentation and examples
- Full test coverage
- Modular design supporting both script and import usage
