# Exercise: Loops

# 1. Loop over a list of numbers 1-10 and print only the even ones.
# 2. Use a while loop to count down from 5 to 1.
# 3. Use enumerate to print each tool in a list with its position.

numbers = list(range(1, 11))
for n in numbers:
    if n % 2 == 0:
        print("Even:", n)

count = 5
while count >= 1:
    print("Countdown:", count)
    count -= 1

tools = ["Python", "SQL", "Airflow","ETL", "Spark"]
for position, tool in enumerate(tools, start=1):
    print(f"{position}: {tool}")
