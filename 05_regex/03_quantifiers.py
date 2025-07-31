import os
# os.system('clear')
os.system('cls')

import re

# -------------------------------------
print('')
text: str = 'aaaba'
pattern: str = r'a*'
result_all: list[any] = re.findall(pattern=pattern, string=text)

print(result_all)

# -------------------------------------
print('')
text = 'boat cow mouse car sea white black apple orange hospital'
pattern = r'a+'
result_all = re.findall(pattern=pattern, string=text)

print(result_all)

# -------------------------------------
print('')
text = 'aaabacb'
pattern = r'a?b'
result_all = re.findall(pattern=pattern, string=text)

print(result_all)

# -------------------------------------
print('')
text = 'aaaaaa aa a aaaa'
pattern = r'a{3}'
result_all = re.findall(pattern=pattern, string=text)

print(result_all)

# -------------------------------------
print('')
text = 'aaa aa a aa aaaa a a'
pattern = r'a{2,3}'
result_all = re.findall(pattern=pattern, string=text)

print(result_all)

# -------------------------------------
print('')
text = 'lion house bat cow mouse donkey passion watermelon fruit'
pattern = r'\b\w{3,5}\b'
result_all = re.findall(pattern=pattern, string=text)

print(result_all)

# -------------------------------------
print('')
text = 'lion house bat cow mouse donkey passion watermelon fruit'
pattern = r'\b\w{6,}\b'
result_all = re.findall(pattern=pattern, string=text)

print(result_all)