from playwright.sync_api import Page
class RegisterPage(Page):
    URL = "https://www.automationexercise.com/"
    def __init__(self, page: Page):
        self.page = page
        self.nav_signup_login_link = page.get_by_role("link", name="Signup / Login")
        self.logged_in_text = page.locator("li", has_text="Logged in as")
        self.delete_account_link = page.get_by_role("link", name="Delete Account")

        # Step 1: Form New User Signup
        self.name_input = page.locator("input[data-qa='signup-name']")
        self.email_input = page.locator("input[data-qa='signup-email']")
        self.signup_button = page.locator("button[data-qa='signup-button']")

        # Step 2: Form Enter Account Information
        self.title_mr_radio = page.get_by_role("radio", name="Mr.")
        self.password_input = page.locator("input[data-qa='password']")
        self.days_select = page.locator("#days")
        self.months_select = page.locator("#months")
        self.years_select = page.locator("#years")
        self.newsletter_checkbox = page.get_by_role("checkbox", name="Sign up for our newsletter!")

        # Step 3: Address Information
        self.first_name_input = page.locator("input[data-qa='first_name']")
        self.last_name_input = page.locator("input[data-qa='last_name']")
        self.company_input = page.locator("input[data-qa='company']")
        self.address1_input = page.locator("input[data-qa='address']")
        self.address2_input = page.locator("input[data-qa='address2']")
        self.country_select = page.locator("#country")
        self.state_input = page.locator("input[data-qa='state']")
        self.city_input = page.locator("input[data-qa='city']")
        self.zipcode_input = page.locator("#zipcode")
        self.mobile_number_input = page.locator("input[data-qa='mobile_number']")

        # Action Buttons
        self.create_account_button = page.locator("button[data-qa='create-account']")
        self.continue_button = page.locator("a[data-qa='continue-button']")

    def navigate(self):
        self.page.goto(self.URL)

    def go_to_signup(self):
        self.nav_signup_login_link.click()

    def submit_initial_signup(self, name: str, email: str):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.signup_button.click()

    def fill_account_details(self, password: str, day: str, month: str, year: str):
        self.title_mr_radio.check()
        self.password_input.fill(password)
        self.days_select.select_option(day)
        self.months_select.select_option(month)
        self.years_select.select_option(year)
        self.newsletter_checkbox.check()

    def fill_address_details(self, user_info: dict):
        self.first_name_input.fill(user_info["first_name"])
        self.last_name_input.fill(user_info["last_name"])
        self.company_input.fill(user_info.get("company", ""))
        self.address1_input.fill(user_info["address1"])
        self.address2_input.fill(user_info.get("address2", ""))
        self.country_select.select_option(user_info["country"])
        self.state_input.fill(user_info["state"])
        self.city_input.fill(user_info["city"])
        self.zipcode_input.fill(user_info["zipcode"])
        self.mobile_number_input.fill(user_info["mobile"])
        self.create_account_button.click()

    def click_continue(self):
        self.continue_button.click()
        self.handle_google_ad()

    def delete_account(self):
        self.delete_account_link.click()
        self.continue_button.click()
        self.handle_google_ad()

    def handle_google_ad(self):

        try:
            ad_iframe = self.page.frame_locator("iframe[name='aswift_2']")
            ad_button = ad_iframe.get_by_role("button", name="Close ad")
            if ad_button.is_visible(timeout=3000):
                ad_button.click()
        except Exception:
            pass



