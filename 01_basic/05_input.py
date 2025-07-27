my_name: str = ""
my_age: int = 0
my_age_after: int = 20
my_country: str = ""
my_city: str = ""
question_name: str = "What is your name?"
question_age: str = "How old are you?"
question_country_city: str = "In what country and city do you live?"
response_name: str = "Hello welcome, your name is"
response_age: str = "You age is"
response_age_two: str = "years old"
response_country_city: str = "You live in"
response_final: str = ""

print(question_name)
my_name = input()
print(question_age)
my_age = int(input())

response_final = f"{response_name} {my_name}"
print(response_final)

response_final = f"{response_age} {my_age} {response_age_two}"
print(response_final)

# --------------------------------------------------------------------------
my_name = input(question_name + "\n")
my_age = int(input(question_age + "\n"))

response_final = f"{response_name} {my_name}"
print(response_final)

response_final = f"{response_age} {my_age} {response_age_two}"
print(response_final)

# --------------------------------------------------------------------------
my_country, my_city = input(question_country_city + "\n").split()

response_final = f"{response_country_city} {my_country}, {my_city}"
print(response_final)