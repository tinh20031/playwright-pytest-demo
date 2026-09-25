import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password, is_success", [
    ("Admin", "admin123", True),
    ("locked_out_user", "secret_sauce", False),
    ("standard_user", "wrong_pass", False),
    ("", "secret_sauce", False),
])
def test_login_page(page: Page, username, password, is_success):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(username, password)

    if is_success:
        # Nếu đăng nhập thành công: chuyển sang trang dashboard
        expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    else:
        # Nếu thất bại: kiểm tra xuất hiện alert "Invalid credentials" HOẶC thông báo "Required"
        expect(login_page.alert_invalid.or_(login_page.required_field).first).to_be_visible()
        # Đảm bảo URL vẫn ở trang login
        expect(page).to_have_url(login_page.URL)