
import os
#os.system('clear')
os.system('cls')

print("5 > 3:", 5 > 3)
print("5 < 3:", 5 < 3)
print("5 == 5:", 5 == 5)
print("5 != 3:", 5 != 3)
print("5 >= 5:", 5 >= 5)
print("5 <= 3:", 5 <= 3)

# ------------------------------------
# lexicograficas
print("")
print("'apple' < 'pear':", "apple" < "pear")
print("'hello' > 'Hello':", "hello" > "Hello")
print("'hello' == 'Hello':", "hello" == "Hello")

# ------------------------------------
print("")
print("True and True:", True and True)
print("True and False:", True and False)
print("True or False:", True or False)
print("False or False:", False or False)
print("not True:", not True)
print("not False:", not False)

# ------------------------------------
print("")
print("A     B     A and B")
print("True  True ", True and True)
print("True  False", True and False)
print("False True ", False and True)
print("False False", False and False)

# ------------------------------------
print("")
print("A     B     A or B")
print("True  True ", True or True)
print("True  False", True or False)
print("False True ", False or True)
print("False False", False or False)

# ------------------------------------
print("")
print("A      not A")
print("True  ", not True)
print("False ", not False)
