import os
#os.system('clear')
os.system('cls')

list_1: list[int] = [0, 1, 2, 3, 4]
list_1.append(list_1[-1] + 1)
list_1.append(list_1[-1] + 1)
print(list_1)

list_2: list[str] = ['a', 'b', 'c', 'd']
list_2.append('e')
print(list_2)

list_2.insert(2, '@')
print(list_2)

list_2.extend(['caracas', 'valencia'])
print(list_2)

list_2.remove('@')
print(list_2)

list_2.remove('caracas')
print(list_2)

list_2.remove('valencia')
print(list_2)

list_2_value = list_2.pop()
print(list_2)
print(list_2_value)

list_2_value = list_2.pop(2)
print(list_2)
print(list_2_value)

del list_2[1]
print(list_2)

list_2.clear()
print(list_2)

del list_1[3:]
print(list_1)

del list_1[1:2]
print(list_1)

# -----------------------------------------------------
print("")
list_3: list[int] = [3, 0, 18, 21, 2014, -3, -2, -5, 10, 12, 5]
list_4: list[int] = []
list_4 = list_3[:]
print(list_3)
print(list_4)

print("")
list_4.sort()
list_5: list[int] = sorted(list_3)
print("list_3:", list_3)
print("list_4:", list_4)
print("list_5:", list_5)

# -----------------------------------------------------
print("")
list_6: list[str] = ["apple", "pear", "banana", "orange", "lemon"]
list_7: list[str] = list_6[:]
list_8: list[str] = sorted(list_6)
list_9: list[str] = ["apple", "pear", "Banana", "Orange", "banana", "lemon", "orange"]
list_10: list[str] = list_9[:]
list_7.sort()
list_9.sort()

print(list_6)
print(list_7)
print(list_8)
print(list_9)
print(list_10)

list_10.sort(key=str.lower)
print(list_10)