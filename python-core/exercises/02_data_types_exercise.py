# Exercise: Data Types

# 1. Create one variable each of type int, float, bool, str, and list.
# 2. Print the value and type of each variable.
# 3. Convert the int to a string and the string back to an int.

age = 23
height = 5.6
is_learning = True
city = "Visakhapatnam"
scores = [88, 92, 79]

print(type(age), age)
print(type(height), height)
print(type(is_learning), is_learning)
print(type(city), city)
print(type(scores), scores)

age_str = str(age)
age_back_to_int = int(age_str)
print("Age as string:", age_str, type(age_str))
print("Age back to int:", age_back_to_int, type(age_back_to_int))
