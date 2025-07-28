import os
# os.system('clear')
os.system('cls')

# ---------------------------------------------------
print("")
numbers_range: range = range(0, 10)

for number in numbers_range:
    print(number)

# ---------------------------------------------------
print("")
numbers_range_even = range(0, 10, 2)

for number in numbers_range_even:
    print(number)

# ---------------------------------------------------
print("")
numbers_range = range(-10, 0)

for number in numbers_range:
    print(number)

# ---------------------------------------------------
print("")
numbers_range = range(10, 0, -1)

for number in numbers_range:
    print(number)

# ---------------------------------------------------
print("")
numbers_range = range(0, 10)
numbers_list: list[int]
numbers_list = list(numbers_range)
print(numbers_list)

# ---------------------------------------------------
print("")
for _ in range(0, 5):
    print(f"value: {_}")