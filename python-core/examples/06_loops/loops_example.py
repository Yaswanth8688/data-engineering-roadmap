# Loops example

skills = ["Python", "SQL", "Airflow", "Spark"]

# Basic for loop
for skill in skills:
    print("Skill:", skill)

# for loop with enumerate (index + value)
for index, skill in enumerate(skills, start=1):
    print(f"{index}. {skill}")

# for loop with range
for i in range(5):
    print("Count:", i)

# while loop
attempts = 0
while attempts < 3:
    print("Attempt number:", attempts + 1)
    attempts += 1

# break and continue
for skill in skills:
    if skill == "SQL":
        continue  # skip SQL
    if skill == "Spark":
        break  # stop once we reach Spark
    print("Processing:", skill)

# zip: loop over two lists together
years_exp = [2, 3, 1, 1]
for skill, years in zip(skills, years_exp):
    print(f"{skill}: {years} year(s) of experience")

# Nested loop
matrix = [[1, 2], [3, 4]]
for row in matrix:
    for value in row:
        print("Value:", value)
