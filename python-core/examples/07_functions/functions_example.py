"""Functions example.

This module demonstrates defining and calling functions in Python.
"""


def greet(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def add(a: int, b: int = 10) -> int:
    """Add two numbers. b defaults to 10 if not provided."""
    return a + b


def describe_employee(name: str, *, role: str = "Data Engineer") -> str:
    """Keyword-only argument example (role must be passed by name)."""
    return f"{name} works as a {role}."


def total_experience(*years) -> int:
    """*args example: accept any number of positional arguments."""
    return sum(years)


def build_profile(**details) -> dict:
    """**kwargs example: accept any number of keyword arguments."""
    return details


print(greet("Yaswanth"))
print("add(5):", add(5))
print("add(5, 20):", add(5, 20))
print(describe_employee("Yaswanth", role="Analytics Engineer"))
print("Total experience:", total_experience(2, 3, 1))
print("Profile:", build_profile(name="Yaswanth", city="Visakhapatnam"))

# Lambda: small anonymous function
square = lambda x: x ** 2
print("Square of 6:", square(6))

# Functions as first-class objects
skills = ["python", "sql", "airflow"]
print("Uppercased:", list(map(str.upper, skills)))
print("Long names:", list(filter(lambda s: len(s) > 4, skills)))
