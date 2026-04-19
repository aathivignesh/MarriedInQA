import json

import pytest
from playwright.sync_api import Playwright, expect
from Married.test_signinuser import usersignin
from Married.test_loginuser import userlogin

with open('credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    credentialslist = test_data['usercredentials']

@pytest.mark.parametrize('testdatacredentials', credentialslist)
def test_frontpagefunc(playwright:Playwright, testdatacredentials):

    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
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