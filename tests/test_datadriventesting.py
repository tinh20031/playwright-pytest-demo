from operator import truediv

import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password, is_success", [
    ("Admin", "admin123", True),
    ("locked_out_user", "secret_sauce", False),
    ("standard_user", "wrong_pass", False),
    ("", "secret_sauce", False),
    ("", "secret_sauce", True),
])
def test_login_page(page: Page, username, password, is_success):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)

    if is_success:
        expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        print(f"\n[PASS - SUCCESS]: Tài khoản '{username}' đăng nhập thành công vào Dashboard.")
    else:
        # Bắt buộc xuất hiện thông báo lỗi
        expect(login_page.alert_invalid.or_(login_page.required_field).first).to_be_visible()
        expect(page).to_have_url(login_page.URL)

        # In thông báo để biết web đã chặn chuẩn
        if username == "":
            print(f"\n[PASS - BLOCKED]: Để trống Username -> Hệ thống chặn và hiện lỗi 'Required'.")
        else:
            print(f"\n[PASS - BLOCKED]: Tài khoản sai '{username}' -> Hệ thống chặn và hiện lỗi 'Invalid credentials'.")