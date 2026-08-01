"""Strings example.

This module demonstrates string operations and Python docstrings.
"""

message = "Hello, Data Engineering!"
name = 'Yaswanth'

# Concatenate strings
welcome = message + " " + name
print(welcome)

# String formatting
formatted = f"{name} has {len(message)} characters in the message."
print(formatted)

# Slicing
print('First 5 chars:', message[:5])
print('Last 10 chars:', message[-10:])

# Replace and upper/lower
print(message.replace('Data', 'Python'))
print(message.upper())
print(message.lower())


def greet(person_name: str) -> str:
    """Return a greeting for the given person.

    Args:
        person_name: The name of the person to greet.

    Returns:
        A greeting string including the person's name.
    """
    return f"Hello, {person_name}!"

print(greet(name))
