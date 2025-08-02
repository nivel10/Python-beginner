import os
import re
from playwright.sync_api import Page, expect

match os.name:
    case 'nt':
        os.system('cls')
    case 'posix':
        os.system('clear')
    case 'java':
        print(os.name)

# -----------------------------------------------------
print('')
def test_has_title(page: Page):
    page.goto('https://playwright.dev/')

    expect(page).to_have_title(re.compile('Playwright'))
    # expect(page).to_have_title(re.compile('Midu'))

def test_get_started_link(page: Page):
    page.goto('https://playwright.dev/')

    page.get_by_role('link', name='Get started').click()

    expect(page.get_by_role('heading', name='Installation')).to_be_visible()