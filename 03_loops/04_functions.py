import os
# os.system('clear')
os.system('cls')

# ---------------------------------
print("")
def greet():
    print('Hello...!!!')

greet()

# ---------------------------------
print("")
def greet_to(name: str):
    print(f'Hello {name}...!!!')

greet_to('Nikole')
greet_to('Carlos')

# ---------------------------------
# docString: """Sum two numbers and returns the result"""
print("")
def sum(a: int | float, b: int | float):
    """Sum two numbers and returns the result"""
    result: int | float = 0
    result = a + b
    return result

result: int | float = sum(5, 12)
print(result)
print(sum.__doc__)

print(sum(20, 14))
print(sum.__doc__)

result = sum(1981.70, 14.00)
print(result)
print(sum.__doc__)

# ---------------------------------
# docString: """Subtract two numbers and returns the result"""
print("")
def subtract(a: int | float, b: int | float):
    """Subtract two numbers and returns the result"""
    result: int | float = 0
    result = a - b
    return result

result: int | float = 0
result = subtract(2014, 12)
print(result)
print(subtract.__doc__)

result = subtract(2014.12, 5.00)
print(result)
print(subtract.__doc__)

print("")
help(subtract)