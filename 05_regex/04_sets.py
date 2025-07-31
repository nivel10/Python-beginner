import os
# os.system('clear')
os.system('cls')

import re

# --------------------------------------------
print('')
# text: str = 'ni.vel_10'
text: str = 'ni.v#l_10'
# pattern: str = r'[\w._%+-]'
pattern: str = r'^[\w._%+-]+$'

result = re.search(pattern=pattern, string=text)

if result:
    print('The user name is valid.')
else:
    print('The user name is not valid.')

# --------------------------------------------
print('')
text = 'Hello world'
pattern = r'[aeiou]'
result_all: list[any] = re.findall(pattern=pattern, string=text)

print(result_all)

# --------------------------------------------
print('')
text = 'man ban ran fan tan ram'
pattern = r'[fmr]an'
result_all = re.findall(pattern=pattern, string=text)

print(result_all)

# --------------------------------------------
print('')
text = 'Hello world.'
pattern = r'[^aeiou]'
result_all = re.findall(pattern=pattern, string=text)

print(result_all)