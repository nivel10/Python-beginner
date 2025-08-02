import os
import requests
from bs4 import BeautifulSoup

match os.name:
    case 'nt':
        os.system('cls')
    case 'posix':
        os.system('clear')
    case 'java':
        print(os.name)

web_scraping: object = {
    'url': 'https://www.apple.com/es/shop/buy-mac/macbook-air/',
    'html': '',
}

response: object = {}
response = requests.get(url=web_scraping['url'])

if response.status_code == 200:
    print('The request is successfully')

web_scraping['html'] = response.text
soup = BeautifulSoup(web_scraping['html'], 'html.parser')

# print(soup.prettify())

title_tag: str = soup.title
if title_tag:
    print(f'The title of the website is: {title_tag.text}')
    print(f'The title of the website is: {title_tag.string}')