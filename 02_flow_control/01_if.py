import os
#os.system("clear")
os.system("cls")

my_age: int = 18
my_age_two: int = 17
my_test_note: int = 7
have_license: bool = True
msg_legal_age: str = "You are of legal age"
msg_not_legal_age: str = "You are not legal age"
msg_congratulations: str = "Congratulations...!!!"
msg_sorry: str = "Sorry :/"
msg_carrie_return: str = " "
msg_final: str = ""
is_weekend: bool = False
have_money: bool = True

print(msg_carrie_return)

if my_age >= 18:
    print(f"{msg_legal_age}: {my_age}")
    print(msg_congratulations)

# ------------------------------------------------
print(msg_carrie_return)
if my_age_two >= 18:
    print(f"{msg_legal_age}: {my_age_two}")
    print(msg_congratulations)
else:
    print(f"{msg_not_legal_age}: {my_age_two}")
    print(msg_sorry)

# ------------------------------------------------
print(msg_carrie_return)
if my_test_note >= 9:
    print(f"Excellent..!!! ({my_test_note})")
elif my_test_note >= 7:
    print(f"Good ({my_test_note})")
elif my_test_note >= 5:
    print(f"Fine ({my_test_note})")
else:
    print(f"Not good. {msg_sorry} ({my_test_note})")

# ------------------------------------------------
print(msg_carrie_return)
if my_age_two >= 18 and have_license:
    print("You can drive...!!!")
else:
    print(f"You can not drive. {msg_sorry}")

# ------------------------------------------------
print(msg_carrie_return)
if my_age >= 18 or have_license:
    print("You can drive...!!!")
else:
    print(f"You can ot drive. {msg_sorry}")

# ------------------------------------------------
print(msg_carrie_return)
if is_weekend:
    print(f"Yes, is weekend. {msg_congratulations}")

if not is_weekend:
    print(f"Is not weekend. {msg_sorry}")

# ------------------------------------------------
print(msg_carrie_return)
if my_age_two >= 18:
    if have_money:
        print("You can go to the disco")
    else:
        print("You need save money, from that you can go to the disco")
else:
    print(f"You can't go to the disco. {msg_sorry}")

# ------------------------------------------------
print(msg_carrie_return)
if my_age < 18:
    print(f"You can't go to the disco. {msg_sorry}")
elif have_money:
    print("You can go to the disco")
else:
    print("Better stay home")

# ------------------------------------------------
print(msg_carrie_return)
my_number: int = 5
my_number_two: int = 0

if my_number:
    print(f"This nuber is not zero: {my_number}")

if not my_number_two:
    print(f"This number is zero: {my_number_two}")

# ------------------------------------------------
print(msg_carrie_return)
current_name: str = "this is my name"
current_name_two: str = ""

if current_name:
    print(f"Variable current_name is not empty: {current_name}")

if not current_name_two:
    print(f"Variable current_name_two is empty: {current_name_two}")

# ------------------------------------------------
print(msg_carrie_return)
msg_final = f"{msg_legal_age}: {my_age}. {msg_congratulations}" if my_age >= 18 else f"{msg_not_legal_age}: {my_age}. {msg_sorry}"
print(msg_final)