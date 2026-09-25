import pytest
from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import page

from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password, is_success", [
    ("Admin", "admin123", True),
    ("locked_out_user", "secret_sauce", False),
    ("standard_user", "wrong_pass", False),
    ("", "secret_sauce", False),
])
def test_login_page(page:Page, username, password, is_success):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)

    if is_success:
        expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    else:
        expect.to_have_failure("Login failed")







