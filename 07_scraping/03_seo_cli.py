import os
import requests
import argparse
from bs4 import BeautifulSoup
from urllib.parse import urljoin

match os.name:
    case 'nt':
        os.system('cls')
    case 'posix':
        os.system('clear')
    case 'java':
        print(os.name)

# -----------------------------------------------------
print('')
parser = argparse.ArgumentParser(description='Web scraping to check SEO for a give URL')
parser.add_argument('url', type=str, help='The url of the site you want to scrape and check')

args = parser.parse_args()
url = args.url

response = requests.get(url=url)
if response:
    print('The request is sucessfully')

soup = BeautifulSoup(response.text, 'html.parser')

print(f'\033[34mCheck web site:\033[0m {url}')
print('basic SEO')

title_website = soup.find('title').get_text()
if title_website:
    print(f'The website title is: \033[44m{title_website}\033[0m')
    if len(title_website) < 70:
        print(f'\033[32mThe website title is correct\033[0m')
    else:
        print(f'\033[31mThe website title is incorrect\033[0m')

title_h1 = [title.text for title in soup.find_all('h1')]
if not title_h1:
    print('\033[31mTitles h1 not found.\033[0m')
elif len(title_h1) > 1:
    print('\033[31mThere is more than one title\033[0m')
    for title in title_h1:
        print(title)
else:
    print('There is one title in the website')
    print(title_h1)