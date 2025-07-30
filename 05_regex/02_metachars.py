import os
# os.system('clear')
os.system('cls')

# -----------------------------------
print('')
import re

text: str = 'Hello world, H$llo again, H3llo again...!!!'
# odc is same one characters
pattern: str = 'H.llo'

result: list[any] = re.findall(pattern=pattern, string=text)

if result:
    print(result)
else: 
    print('Pattern not found.')


# -----------------------------------
print('')

# odc is same one characters
pattern: str = r'H.llo'

result = re.findall(pattern=pattern, string=text)

if result:
    print(result)
else: 
    print('Pattern not found.')

# -----------------------------------
print('')

text = 'My house is white. My car es black.'
pattern = r'\.'

result  = re.findall(pattern=pattern, string=text)

if result:
    print(result)
else: 
    print('Pattern not found.')

# -----------------------------------
print('')

text = 'The phone number is: 0123456789'
# parttern = r'\d'
# parttern = r'\d\d'
# parttern = r'\d\d\d'
pattern = r'\d{10}'

result = re.findall(pattern=pattern, string=text)

if result:
    print(result)
else: 
    print('Pattern not found.')

# -----------------------------------
print('')
text = 'My number phone is +58 2128769857. Take note'
pattern = r'\+58 \d{10}'

found = re.search(pattern=pattern, string=text)

if found:
    print(f'Number phone: {found.group()}')
else:
    print('Pattern not found.')

# -----------------------------------
print('')

# \w: (a-z, A-Z, 0-9, _)
# text = 'nivel_10'
text = '@nivel_10-%)'
pattern = r'\w'
result_all: list[any] = re.findall(pattern=pattern, string=text)

print(result_all)

# -----------------------------------
print('')

# \s: (' ', \n, \t)
text = 'Hello world\nHow are you?\t'
pattern = r'\s'

result_all = re.findall(pattern=pattern, string=text)
print(result_all)

# -----------------------------------
print('')
# ^: begin text
# text = "@nivel_10"
text = "nivel_10"
pattern = r'^\w'

found = re.search(pattern=pattern, string=text)

if found:
    print(f'The user name: {text} is valid.')
else:
    print(f'The user name: {text} is not valid.')

# -----------------------------------
print('')
# ^: begin text
text = '+58 2127876549'
pattern = r'^\+\d{1,3} '

found = re.search(pattern=pattern, string=text)

if found:
    print(f'The phone number: {text} is valid')
else:
    print(f'The phone number: {text} is not valid')