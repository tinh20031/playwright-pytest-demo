import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_example(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("Admin", "admin123")
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")



