import os
import re
import requests

match os.name:
    case 'nt':
        os.system('cls')
    case 'posix':
        os.system('clear')
    case 'java':
        print(os.name)

# ------------------------------------------
print('')
response: object = {}
result: object = {}
web_scraping: object = {
    'url': 'https://www.apple.com/es/shop/buy-mac/macbook-air/',
    'html': '',
}

response = requests.get(url=web_scraping['url'])

# print(response.status_code)
# print(response.text)

if response.status_code == 200:
    print('The request is successfully')

web_scraping['html'] = response.text

# price_pattern = r'<span class="rc-prices-fullprice">(.?+)</span>'
patterns: object = {
    'title': r'<title>(.*?)</title>',
    'price': r'<span class="rc-prices-fullprice">(.*?)</span>'
}

match = re.search(pattern=patterns['price'], string=web_scraping['html'])
if match:
    print(f'The price of the item is: {match.group(1)}')

match = re.search(pattern=patterns['title'], string=web_scraping['html'])
if match:
    print(f'The title of the items is: {match.group(1)}')