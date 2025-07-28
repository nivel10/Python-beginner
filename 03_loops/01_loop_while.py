import os
# os.system('clear')
os.system('cls')

print("")
count: int = 0

while count < 5:
    print(count)
    count += 1

# ---------------------------------------
print("")
count = 0
while True:
    print(count)
    count +=1

    if count == 10:
        break

# ---------------------------------------
print("")
count = 1
while count <= 100:
    print(count)
    if count % 5 == 0:
        print(f"result: {count}")
        break

    count += 1

# ---------------------------------------
print("")
count = 0

while count <= 15:
    count += 1

    if count % 2 == 0:
        continue

    print(count)

# ---------------------------------------
print("")
count = 0
while count <= 10:
    count += 1

    if count % 2 == 0:
        continue

    print(count)
else:
    print('The loop has ended')


# ---------------------------------------
print("")
count = 0
while count <= 10:
    count += 1

    if count % 2 == 0:
        continue

    print(count)

    if count == 5:
        break
else:
    print('The loop has ended')

# ---------------------------------------
# print("")
# number_max: int = 10
# number_current: int = 0
# # number_catch: int = 0
# user_msg: str = f"Please, you must enter a number greater than {number_max}\n"

# while number_current <= 10:
#     print(user_msg)
#     number_current = int(input())

# print(f"Your number is {number_current}")

print("")
number_max: int = 10
number_current: int = 0
user_input: str = ""
user_msg: str = f"Please, you must enter a number greater than {number_max}\n"

while number_current <= 10:
    try:
        print(user_msg)
        user_input = input()
        number_current = int(user_input)
    except:
        #print("")
        print(f"\nThe entered values: '{user_input}'\nIs not valid, It must be a number. \nTry again\n")

print(f"Your number is {number_current}")