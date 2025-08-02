import os
from playwright.sync_api import sync_playwright

match os.name:
    case 'nt':
        os.system('cls')
    case 'posix':
        os.system('clear')
    case 'java':
        print(os.name)

# -----------------------------------------------------
print('')

url: str = 'https://midu.dev/'

with sync_playwright() as p:
    # browser = p.chromium.launch(headless=False, slow_mo=2000)
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url)

    first_article_anchor = page.locator('article a').first
    first_article_anchor.click()

    page.wait_for_load_state()

    first_image = page.locator('main img').first
    # print(first_image.get)
    image_src = first_image.get_attribute('src')
    print(f'The image of the first curso is this: {image_src}')

    browser.close()