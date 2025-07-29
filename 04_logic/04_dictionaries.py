import os
# os.system('clear')
os.system('cls')

# ----------------------------------------
print('')

people = {
    'name': 'nivel10',
    'age': 44,
    'is_student': True,
    'notes': [8, 9, 7.5, 10, 9.2],
    'socials': {
        'twitter': '@nivel10',
        'facebook': 'nivel10',
        'instagram': '@nivel10',
    }
}

print(people['name'])
print(people['notes'])
print(people['notes'][2])
print(people['socials'])
print(people['socials']['facebook'])

print('')
people['name'] = 'Nivel_10'
print(people['name'])

print('')
print(people)

print('')
del people['age']
print(people)

print('')
is_student: bool = people.pop('is_student')
print(people)
print(f'is student: {is_student}')

print('')
a: dict[str | int | bool] = {'name': 'nivel10', 'age': 44, 'is_student': True, }
b: dict[str | int | bool] = {'name': 'nivel_10', 'address': 'some place', }

print(a)
print(b)

print('')
a.update(b)
print(a)

print('')
result: bool = False
result = 'nombre' in people
print(result)

result = 'name' in people
print(result)

print('')
print(f'keys: {people.keys()}')
print(f'values: {people.values()}')
print(f'items: {people.items()}')

# ----------------------------------------
print('')
def find_first_sum(nums: list[int | float], goal: int | float) -> list[int | float]:
    
    dictionary = {}
    missing: int | float = 0
    for index, num in enumerate(nums):
        missing = goal - num
        if missing in dictionary:
            return [dictionary[missing], index]
        else:
            dictionary[num] = index
 
    return None

nums: list[int | float] = [0, 2, 2, 3, 5, 6]
goal: int | float = 8

result: int | float = 0
result = find_first_sum(nums=nums, goal=goal)
print(result)

print('')
result = find_first_sum(nums=nums, goal=19)
print(result)