import os
# os.system('clear')
os.system('cls')

# ------------------------------------------------
print("")
fruits: list[str] = ['apple', 'pear', 'peach', 'lemon', 'strawberry', 'grape', 'watermelon', 'passion fruit']
animals: list[str] = ['parrot', 'fish', 'cat', 'bird', 'dog', 'cow', 'shark', 'monkey', 'donkey', 'mouse', 'bat',]
numbers: list[int] = [0, 1, 2, 3]
fruit_name: str = fruits[4]
for fruit in fruits:
    print(f'Fruit: {fruit}')

for character in fruit_name:
    print(character)

# ------------------------------------------------
print("")
for index, fruit in enumerate(fruits):
    print(f"Fruit: {fruit}. Index: {index}")

# ------------------------------------------------
print("")
for number in numbers:
    for fruit in fruits:
        print(f"number - fruit: {number} -> {fruit}")

# ------------------------------------------------
print("")
animal_find:str = 'bird'
for index, animal in enumerate(animals):
    if animal == animal_find:
        print(f'animal: {animal} - value find: {animal_find} - index: {index}')
        break

# ------------------------------------------------
print("")
animal_find:str = 'bird'
for index, animal in enumerate(animals):
    if animal == animal_find:
        continue

    print(f'animal: {animal} - value find: {animal_find} - index: {index}')


# ------------------------------------------------
print("")
animals_find: list[str] = ['bird', 'cat', 'fish']
animal_is_find: bool = False
for index, animal in enumerate(animals):
    animal_is_find =  animals_find.count(animal)
    if animal_is_find:
        continue

    print(f'animal: {animal} - value find: {animal_find} - index: {index}')

# ------------------------------------------------
print("")
animals_upper_case: list[str] = [animal.upper() for animal in animals]

for index, animal in enumerate(animals):
    print(f"animal (lowerCase): {animal} - (upperCase): {animals_upper_case[index]}")

# ------------------------------------------------
print("")
numbers += [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
events: list[int] = []
events = [number for number in numbers if number % 2 == 0]

print(events)