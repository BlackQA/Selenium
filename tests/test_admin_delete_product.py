from pages.admin_delete_product_pages import AdminProductDelete
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_delete_product(browser, base_url):

    username = "user"
    password = "bitnami"

    admin_product_delete = AdminProductDelete(browser, base_url)
    admin_product_delete.open()

    try:
        admin_product_delete.enter_username(username)
        admin_product_delete.enter_password(password)
        admin_product_delete.click_login_button()
    except Exception as e:
        assert False, f"Ошибка при входе в систему: {e}"

    try:
        admin_product_delete.click_catalog_button()
        admin_product_delete.click_product_button()
    except Exception as e:
        assert False, f"Ошибка при навигации к странице Products: {e}"

    try:
        admin_product_delete.click_checkbox_button()
    except Exception as e:
        assert False, f"Ошибка при выборе товара для удаления: {e}"

    try:

        delete_button = admin_product_delete.wait.until(
            EC.element_to_be_clickable(admin_product_delete.Delete_button)
        )
        delete_button.click()
    except Exception as e:
        assert False, f"Кнопка удаления не найдена или не кликабельна: {e}"

    try:

        confirm_alert = WebDriverWait(browser, 5).until(
            EC.alert_is_present(), "Confirm алерт не появился"
        )

        #  print(f"Текст confirm алерта: {confirm_alert.text}")

        confirm_alert.accept()
        time.sleep(1)

    except Exception as e:
        assert False, f"Ошибка при обработке confirm алерта: {e}"

    try:
        admin_product_delete.get_success_message(
            expected_text="Success: You have modified products!"
        )
    except Exception as e:
        assert False, f"Ошибка при проверке текста сообщения: {e}"
