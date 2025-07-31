import os
# os.system('clear')
os.system('cls')

# ---------------------------------------
print('')
import urllib.request
import json

try:
    api_url: str = 'https://jsonplaceholder.typicode.com/posts/'
    response = urllib.request.urlopen(api_url)
    data = response.read()
    data_json = json.loads(data.decode('utf-8'))

    print(data_json)

    response.close()
except urllib.error.URLError as e:
    print('Error: {e}')