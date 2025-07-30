import os
# os.system('clear')
os.system('cls')

# ---------------------------------------
print('')
import re
pattern: str = 'Hello'
text: str = 'Hello world...!!!'
result = re.search(pattern=pattern, string=text)

if result:
    print('Pattern is finded on the text')
else:
    print('Pattern is not finded on the text')

print('')
print(f'Pattern: {result.group()}')
print(f'Initial pattern coincidence: {result.start()}')
print(f'End pattern coincidence: {result.end()}')


# --------------------------------------------
print('')
pattern = 'Ipsum'
text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
result_list: list[any] = re.findall(pattern=pattern, string=text)

print(result_list)
print(f'Quantity: {len(result_list)}')

# --------------------------------------------
print('')
pattern = 'Ip.um'
text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipzum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipcum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Iptum."
result_list: list[any] = re.findall(pattern=pattern, string=text)

print(result_list)
print(f'Quantity: {len(result_list)}')

# --------------------------------------------
print('')
pattern = 'Ip.um'
text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipzum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipcum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Iptum."
result_iter = re.finditer(pattern=pattern, string=text)

for result in result_iter:
    print(f'pattern: {result.group()} - start: {result.start()} - end: {result.end()}')