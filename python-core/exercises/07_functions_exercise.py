# Exercise: Functions

# 1. Write a function that takes a name and returns a greeting.
# 2. Write a function that takes a list of numbers and returns their average.
# 3. Write a function using *args that returns the total of all arguments.


def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to Data Engineering."


def average(numbers: list) -> float:
    return sum(numbers) / len(numbers)


def total(*values) -> float:
    return sum(values)


print(greet("Yaswanth"))
print("Average:", average([10, 20, 30]))
print("Total:", total(1, 2, 3, 4,5, 6, 7, 8, 9, 10))
