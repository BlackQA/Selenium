import pytest
from pages.logout_admin_pages import LogoutAdminPages
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def logout_admin_page(browser, base_url):
    logout_page = LogoutAdminPages(browser, base_url)
    logout_page.open()
    return logout_page


def test_logout_admin(logout_admin_page):
    USERNAME = "user"
    PASSWORD = "bitnami"

    logout_admin_page.enter_username(USERNAME)
    logout_admin_page.enter_password(PASSWORD)
    logout_admin_page.click_login_button()

    expected_title_after_login = "Dashboard"
    WebDriverWait(logout_admin_page.browser, 5).until(
        EC.title_contains(expected_title_after_login)
    )
    assert (
        expected_title_after_login in logout_admin_page.get_title()
    ), f"Ожидаемый заголовок '{expected_title_after_login}' не соответствует фактическому заголовку '{logout_admin_page.get_title()}'"

    logout_admin_page.logout()
