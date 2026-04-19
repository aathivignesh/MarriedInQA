from playwright.sync_api import expect


class usersignin():
    def __init__(self,page):
        self.page=page


    def test_signin(self,testdatacredentials):
        self.page.get_by_test_id("tab-signup").click()

        expect(self.page.get_by_label("Email Address")).to_be_visible()
        self.page.get_by_label("Email Address").fill(testdatacredentials["email"])

        expect(self.page.get_by_label("Password")).to_be_visible()
        self.page.get_by_label("Password").fill(testdatacredentials["password"])

        expect(self.page.get_by_label("Phone Number")).to_be_visible()
        self.page.get_by_label("Phone Number").fill(testdatacredentials["phone"])



        self.page.get_by_test_id("select-country-code-hero").click()
        self.page.get_by_role("option", name="🇬🇧 UK +44").get_by_text("🇬🇧UK+44").click()
        expect(self.page.get_by_role("button", name="Google")).to_be_visible()
        expect(self.page.get_by_role("button", name="Login with WhatsApp")).to_be_visible()

        self.page.get_by_test_id("button-create-account-hero").click()

        if (testdatacredentials["expected_result"]) == "empty":
            expect(self.page.get_by_text("Phone number is required")).to_be_visible()
            expect(self.page.get_by_text("Phone number is required")).to_contain_text(testdatacredentials["expected_msg_phone"])
            expect(self.page.get_by_text("Invalid email address")).to_be_visible()
            expect(self.page.get_by_text("Invalid email address")).to_contain_text(testdatacredentials["expected_msg_username"])
            expect(self.page.get_by_text("Password must be at least 6 characters")).to_be_visible()
            expect(self.page.get_by_text("Password must be at least 6 characters")).to_contain_text(testdatacredentials["expected_msg_psswrd"])
        elif (testdatacredentials["expected_result"]) == "invalid":
            expect(self.page.get_by_text("Invalid email address")).to_be_visible()
            expect(self.page.get_by_text("Invalid email address")).to_contain_text(testdatacredentials["expected_msg_username"])
            expect(self.page.get_by_text("Password must be at least 6 characters")).to_be_visible()
            expect(self.page.get_by_text("Password must be at least 6 characters")).to_contain_text(testdatacredentials["expected_msg_psswrd"])

