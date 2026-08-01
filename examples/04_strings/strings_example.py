# Strings example

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
