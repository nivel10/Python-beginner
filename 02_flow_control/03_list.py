import os
# os.system('clear')
os.system('cls')

# -------------------------
print("")
list_1: list[int] = [0, 1, 2, 3, 4]
list_2: list[str] = ["apple", "pear", "banana", "orange", "lemon"]
list_3: list[int | str | float | bool] = [1, "pi", 3.1416, True]
list_4 = []
list_5: list[list[int]] = [[1, 2], [3, 4]]
list_6: list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
matrix_1 = [[0,1], [2, 3], [4, 5]]

print(list_1)
print(list_2)
print(list_3)
print(list_4)
print(list_5)
print(matrix_1)

# -------------------------
print("")
print(list_2[0])
print(list_2[1])
print(list_2[-1])

print(list_5[1][0])
print(list_5[0][1])

# slicing
print(list_1[1:4])
print(list_1[:3])
print(list_1[3:])
# copy 
print(list_1[:])
print(list_6[::2])
print(list_6[::3])
print(list_6[::4])
print(list_6[::-1])

# -------------------------
print("")
list_1[0] = 2014
list_1[1] = 12
list_1[2] = 5
print(list_1)

# -------------------------
print("")
list_1 = list_1 + [1981, 7, 14]
print(list_1)

list_2 += ["watermelon", "strawberry", "grape", "passion fruit"]
print(list_2)