import os
# os.system('clear')
os.system('cls')

# --------------------------------------------------
print("")
def check_is_balanced(text: str = ''):
    text = text.lower()

    count_r: int = 0
    count_j: int = 0

    count_r = text.count('r')
    count_j = text.count('j')

    result: bool = False
    result = count_r == count_j

    print(f'Text: {text}')
    print(f'count r: {count_r}\ncount j: {count_j}')
    return result

result: bool = False
result = check_is_balanced(text='')
print(result)

print("")
result = check_is_balanced(text='this a text, hello world')
print(result)

print("")
result = check_is_balanced(text='resource is just, because r is letter')
print(result)