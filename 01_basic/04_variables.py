my_name = "nivel10"
my_age = 99

print(my_name)
print(my_age)

my_age = 100
print(my_age)

# diamic type
my_age_two = 98
print(my_age_two)

my_age_two = "nivel10"
print(my_age_two)

# hard type
print(10 + int("2"))

# f-string
print(f"Hello, my name is {my_name} and i am {my_age - 22} years old")

my_name, my_age, my_age_two = "nivel10", 99, 100
print(f"name: {my_name}; age: {my_age}; age (two): {my_age_two}" )

# variables conventions name
# snake case
# example: this_is_a_variable

# consts - set define on upper case
MY_CONST = 3.146

# variable types
# variables is dinamics and hard, but not static
# variable type anotations

is_user_logged_in: bool = True
print(is_user_logged_in)

is_user_logged_in = 24
print(is_user_logged_in)
