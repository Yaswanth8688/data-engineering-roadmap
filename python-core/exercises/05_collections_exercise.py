# Exercise: Collections

# 1. Create a list of 3 favorite tools/technologies.
# 2. Create a dictionary describing yourself (name, role, years_exp).
# 3. Add one item to the list and increment years_exp in the dictionary.
# 4. Use a comprehension to build a new list of the tools in uppercase.

tools = ["Python", "SQL", "Airflow"]
me = {
    "name": "Yaswanth",
    "role": "Data Engineer",
    "years_exp": 2,
}

tools.append("Spark")
me["years_exp"] += 1

tools_upper = [tool.upper() for tool in tools]

print("Tools:", tools)
print("Me:", me)
print("Tools (upper):", tools_upper)
