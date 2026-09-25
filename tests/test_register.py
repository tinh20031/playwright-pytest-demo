import time
import pytest
from playwright.sync_api import Page, expect
from pages.register_page import RegisterPage


@pytest.mark.smoke
def test_full_register_and_delete_account(page: Page):
    register_page = RegisterPage(page)
    register_page.navigate()
    register_page.go_to_signup()


    unique_email = f"tinh_{int(time.time())}@gmail.com"
    register_page.submit_initial_signup("tinh", unique_email)



    register_page.fill_account_details("tinh2003", "20", "1", "2003")


    user_info = {
        "first_name": "tinh",
        "last_name": "tran",
        "company": "fpt",
        "address1": "Ho Chi Minh",
        "address2": "District 1",
        "country": "United States",
        "state": "California",
        "city": "San Jose",
        "zipcode": "70000",
        "mobile": "0912345678"
    }
    register_page.fill_address_details(user_info)


    register_page.click_continue()


    expect(register_page.logged_in_text).to_contain_text("tinh")


    register_page.delete_account()