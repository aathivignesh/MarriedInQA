import json

import pytest
from playwright.sync_api import expect

class userlogin():

    def __init__(self,page):
        self.page=page


    def test_loginuser(self,testdatacredentials):

        self.page.get_by_test_id("tab-login").click()
        expect(self.page.get_by_label("Email Address")).to_be_visible()
        self.page.get_by_label("Email Address").fill(testdatacredentials["email"])
        expect(self.page.get_by_label("Password")).to_be_visible()
        self.page.get_by_label("Password").fill(testdatacredentials["password"])
        self.page.get_by_test_id("button-sign-in-hero").click()
        if(testdatacredentials["expected_result"])=="empty":
            expect(self.page.get_by_text("Invalid email address")).to_be_visible()
            expect(self.page.get_by_text("Invalid email address")).to_contain_text(testdatacredentials["expected_msg_username"])
            expect(self.page.get_by_text("Password must be at least 6 characters")).to_be_visible()
            expect(self.page.get_by_text("Password must be at least 6 characters")).to_contain_text(testdatacredentials["expected_msg_psswrd"])
        elif(testdatacredentials["expected_result"])=="invalid":
            expect(self.page.get_by_text("Invalid email address")).to_be_visible()
            expect(self.page.get_by_text("Invalid email address")).to_contain_text(testdatacredentials["expected_msg_username"])
            expect(self.page.get_by_text("Password must be at least 6 characters")).to_be_visible()
            expect(self.page.get_by_text("Password must be at least 6 characters")).to_contain_text(testdatacredentials["expected_msg_psswrd"])
            