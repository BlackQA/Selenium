from pages.admin_delete_product_pages import AdminProductDelete
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest


@pytest.mark.parametrize(
    "username, password, expected_message",
    [
        (
            "user",
            "bitnami",
            "Success: You have modified products!",
        )
    ],
)
def test_delete_product(browser, base_url, username, password, expected_message):

    admin_product_delete = AdminProductDelete(browser, base_url)
    admin_product_delete.open()

    admin_product_delete.enter_username(username)
    admin_product_delete.enter_password(password)
    admin_product_delete.click_login_button()

    admin_product_delete.click_catalog_button()
    admin_product_delete.click_product_button()

    admin_product_delete.click_checkbox_button()

    delete_button = admin_product_delete.wait.until(
        EC.element_to_be_clickable(admin_product_delete.Delete_button)
    )
    delete_button.click()

    confirm_alert = WebDriverWait(browser, 5).until(
        EC.alert_is_present(), "Confirm алерт не появился"
    )

    confirm_alert.accept()
    time.sleep(1)

    admin_product_delete.get_success_message(expected_text=expected_message)
