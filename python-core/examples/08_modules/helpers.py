"""A small local module used by modules_example.py."""

APP_NAME = "python-core"


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit."""
    return (celsius * 9 / 5) + 32
