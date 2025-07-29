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

# ---------------------------------
# params y position
print("")
# docString: """Subtract two numbers and returns the result"""
def multuply(a: int | float = 0, b : int | float = 0):
    """Multiply two numbers and returns te result"""
    result: int | float = 0
    result = a * b
    return result

result: int | float = multuply(2014.05, 12.10)
print(result)

# ---------------------------------
# params by key
print("")
def person_describe(name: str = '', age: int = 0, gender: str = ''):
    """Print information of the person"""
    print(f'Hello my name is: {name}, age: {age}, gender: {gender}')

person_describe('Nikole', 10, 'femenino')
person_describe(gender='masculino', name='Carlos', age=44)

# ---------------------------------
print("")
def sum_args(*args):
    """Sum list of number by args and returns te result"""
    sum: int | float = 0
    for arg in args:
        sum += arg
    
    return sum

result: int | float = 0
result = sum_args(0, 1, 2, -3, 4.5, 2014, 12.05, -65)
print(result)

# ---------------------------------
print("")
def person_describe_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

person_describe_kwargs(name='Nikole', country='Vzla', is_tall=True, city='Caracas', age=10,)
print("")
person_describe_kwargs(age=44, last_name='Herrera', skin='white', eyes_color='brown', is_tall=False)
