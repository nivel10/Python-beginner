import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

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

price_span = soup.find('span', class_='rc-prices-fullprice')
if price_span:
    print(f'The price of the item is: {price_span.text}')

prices_span = soup.find_all('span', class_='rc-prices-fullprice')
if prices_span:
    for price in prices_span:
        print(f'The price of the item is: {price.text}')

items = soup.find_all(class_='rc-productselection-item')
for item in items:
    name = item.find(class_='list-title').text
    price = item.find(class_='rc-prices-fullprice').text
    print(f'The items characteristics {name}\nprice: {price}')

# -------------------------------------------------------------
print('')
# web_scraping['url'] ='https://es.wikipedia.org/wiki/Web_scraping'
web_scraping['url'] ='https://midu.dev'
response = requests.get(url=web_scraping['url'])

if response:
    web_scraping['html'] = response.text
    print('The request is sucessfully')

soup = BeautifulSoup(web_scraping['html'], 'html.parser')

# # # titles_h1 = [title.string for title in soup.find_all('h1')]
# # # print(titles_h1)

# # # titles_h2 = [title.text for title in soup.find_all('h2')]
# # # print(titles_h2)

# # # links = [urljoin(web_scraping['url'], link.get('href')) for link in soup.find_all('a')]
# # # print(links)

# # main_text = soup.find('main').get_text()
# # print(main_text)

# context_text = soup.find('div', {'id': 'mw-content-text'}).get_text()
# print(context_text)

og_image = soup.find('meta', {'property': 'og:image'})
if og_image:
    print(og_image['content'])
else:
    print('The image not found.')

og_image = soup.find('meta', property='og:image')
if og_image:
    print(og_image['content'])
else:
    print('The image not found.')