#!/usr/bin/env python3
"""
Hello World Module
==================

A simple demonstration module that provides greeting functionality.

This module demonstrates basic Python programming concepts including:
- Function definitions
- Docstrings
- Main execution guards
- String formatting

Example:
    Basic usage of the module::

        $ python Hello.py
        Hello, World!

    Or import and use programmatically::

        >>> from Hello import greet, greet_person
        >>> greet()
        'Hello, World!'
        >>> greet_person("Alice")
        'Hello, Alice!'

Attributes:
    DEFAULT_GREETING (str): The default greeting message used by functions.

"""

DEFAULT_GREETING = "Hello"


def greet(greeting=DEFAULT_GREETING, target="World"):
    """
    Generate a greeting message.

    This function creates a customizable greeting message by combining
    a greeting phrase with a target recipient.

    Args:
        greeting (str, optional): The greeting phrase to use. 
            Defaults to DEFAULT_GREETING ("Hello").
        target (str, optional): The recipient of the greeting. 
            Defaults to "World".

    Returns:
        str: A formatted greeting message in the form "{greeting}, {target}!"

    Examples:
        >>> greet()
        'Hello, World!'
        >>> greet("Hi", "Python")
        'Hi, Python!'
        >>> greet(target="Developer")
        'Hello, Developer!'

    Notes:
        - The function is pure and has no side effects
        - All arguments are optional with sensible defaults
        - The returned string always ends with an exclamation mark

    See Also:
        greet_person: A convenience function for greeting people by name
    """
    return f"{greeting}, {target}!"


def greet_person(name, greeting=DEFAULT_GREETING):
    """
    Generate a personalized greeting for a specific person.

    This is a convenience wrapper around the greet() function,
    optimized for greeting individuals by name.

    Args:
        name (str): The name of the person to greet. Required.
        greeting (str, optional): The greeting phrase to use.
            Defaults to DEFAULT_GREETING ("Hello").

    Returns:
        str: A personalized greeting message.

    Raises:
        ValueError: If name is empty or contains only whitespace.

    Examples:
        >>> greet_person("Alice")
        'Hello, Alice!'
        >>> greet_person("Bob", "Hi")
        'Hi, Bob!'
        >>> greet_person("Charlie", greeting="Good morning")
        'Good morning, Charlie!'

    Notes:
        - Name parameter is required and must not be empty
        - Whitespace in names is preserved
        - Function validates input before processing
    """
    if not name or not name.strip():
        raise ValueError("Name cannot be empty or whitespace only")
    
    return greet(greeting=greeting, target=name)


def print_greet(greeting=DEFAULT_GREETING, target="World"):
    """
    Print a greeting message to stdout.

    This function generates and immediately prints a greeting message.
    It's a side-effect producing wrapper around the greet() function.

    Args:
        greeting (str, optional): The greeting phrase to use.
            Defaults to DEFAULT_GREETING ("Hello").
        target (str, optional): The recipient of the greeting.
            Defaults to "World".

    Returns:
        None: This function prints to stdout but returns nothing.

    Examples:
        >>> print_greet()
        Hello, World!
        >>> print_greet("Hi", "there")
        Hi, there!

    Notes:
        - This function has side effects (prints to stdout)
        - For testable code, prefer using greet() and handling output separately
        - Output is sent to stdout with automatic newline
    """
    print(greet(greeting=greeting, target=target))


def main():
    """
    Main entry point for the Hello module.

    This function is called when the module is executed as a script.
    It demonstrates the basic functionality by printing a default greeting.

    Returns:
        None: Exits with status code 0 on success.

    Examples:
        When run as a script::

            $ python Hello.py
            Hello, World!

    Notes:
        - This function only executes when the module is run directly
        - It does not execute when the module is imported
        - Uses the print_greet() function for output
    """
    print_greet()


if __name__ == "__main__":
    # Execute main function when script is run directly
    main()
