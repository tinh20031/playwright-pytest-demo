import re
from playwright.sync_api import Page


class LoginPage:
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

        # Locator alert lỗi sai thông tin lấy chính xác từ codegen
        self.alert_invalid = page.get_by_role("alert").locator("div").filter(
            has_text=re.compile(r"^Invalid credentials$"))

        # Locator text cảnh báo bỏ trống
        self.required_field = page.get_by_text("Required")

    def navigate(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()