import json
import os

import pytest
from playwright.sync_api import Playwright, expect
from test_signinuser import usersignin
from test_loginuser import userlogin

# Get the directory of the current test file
test_dir = os.path.dirname(os.path.abspath(__file__))
credentials_path = os.path.join(test_dir, 'credentials.json')

with open(credentials_path) as f:
    test_data = json.load(f)
    print(test_data)
    credentialslist = test_data['usercredentials']

@pytest.mark.parametrize('testdatacredentials', credentialslist)
def test_frontpagefunc(playwright:Playwright, testdatacredentials):
    # Run headless in CI/CD environments, otherwise show browser
    is_headless = os.getenv('CI', 'false').lower() == 'true' or os.getenv('HEADLESS', 'false').lower() == 'true'
    slow_mo_delay = 100 if is_headless else 1000
    
    browser = playwright.chromium.launch(headless=is_headless, slow_mo=slow_mo_delay)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://stage.marriedin.co/")
    page.get_by_role("link",name="About").click()
    page.get_by_role("link",name="Help",exact=True).click()
    loguser=userlogin(page)
    loguser.test_loginuser(testdatacredentials)
    signuser=usersignin(page)
    signuser.test_signin(testdatacredentials)
    #page.get_by_role("button", name="Login with WhatsApp").click()