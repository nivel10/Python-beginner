my_age: int = 18
my_age_two: int = 17
my_test_note: int = 7
msg_legal_age: str = "You are of legal age"
msg_not_legal_age: str = "You are not legal age"
msg_congratulations: str = "Congratulations...!!!"
msg_sorry: str = "Sorry :/"
msg_carrie_return: str = " "

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
