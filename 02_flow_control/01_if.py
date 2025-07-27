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