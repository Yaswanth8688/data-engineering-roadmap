# Exercise: Strings

# 1. Create a string with your full name.
# 2. Print it in uppercase, lowercase, and reversed.
# 3. Use slicing to print just the first name (assume a space separates names).
# 4. Use an f-string to print how many characters are in the full name.

full_name = "Yaswanth Majji"

print(full_name.upper())
print(full_name.lower())
print(full_name[::-1])

first_name = full_name[:full_name.index(" ")]
print("First name:", first_name)

print(f"'{full_name}' has {len(full_name)} characters.")
