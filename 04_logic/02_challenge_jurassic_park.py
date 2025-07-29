import os
# os.system('clear')
os.system('cls')

# ---------------------------------------------
print('')
def count_carnivore_dinosaur_eggs(eggs: list[int | float]) -> int | float:
    """This funtion count the eggs if total is even then the dinosaur eggs is carnivore"""

    coutn_eggs_even: int | float = 0
    count_eggs_odd: int | float = 0

    for egg in eggs:
        if egg % 2 == 0:
            coutn_eggs_even += egg
        else:
            count_eggs_odd += egg

    return coutn_eggs_even

result: int | float = 0
eggs_list: list[int] = [3, 6, 8, 4, 2, 1,]

result = count_carnivore_dinosaur_eggs(eggs=eggs_list)
print(f'Total eggs: {result}')