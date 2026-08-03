# Collections example

# List: ordered, mutable
skills = ["Python", "SQL", "Airflow"]
skills.append("Spark")
print("Skills:", skills)
print("First skill:", skills[0])

# Tuple: ordered, immutable
coordinates = (40.7128, -74.0060)
print("Coordinates:", coordinates)

# Set: unordered, unique values
tools = {"Python", "SQL", "Python", "Airflow"}
print("Unique tools:", tools)
tools.add("Kafka")
print("After add:", tools)

# Dictionary: key-value pairs
employee = {
    "name": "Yaswanth",
    "role": "Data Engineer",
    "years_exp": 2,
}
print("Employee:", employee)
print("Role:", employee["role"])

employee["years_exp"] += 1
print("Updated years_exp:", employee["years_exp"])

# Iterating a dictionary
for key, value in employee.items():
    print(f"{key}: {value}")

# List comprehension
squares = [n ** 2 for n in range(1, 6)]
print("Squares:", squares)

# Dict comprehension
lengths = {skill: len(skill) for skill in skills}
print("Skill name lengths:", lengths)
