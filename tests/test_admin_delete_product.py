from pages.admin_delete_product_pages import AdminProductDelete
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import allure


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
@allure.feature("Удаление продукта")
@allure.story("Успешное удаление продукта")
def test_delete_product(browser, base_url, username, password, expected_message):

    with allure.step("Создание экземпляра AdminProductDelete"):
        admin_product_delete = AdminProductDelete(browser, base_url)

    with allure.step("Открытие страницы администрирования"):
        admin_product_delete.open()

    with allure.step("Ввод имени пользователя: {username}"):
        admin_product_delete.enter_username(username)

    with allure.step("Ввод пароля: {password}"):
        admin_product_delete.enter_password(password)

    with allure.step("Нажатие кнопки входа в систему"):
        admin_product_delete.click_login_button()

    with allure.step("Навигация к разделу каталога и продуктам"):
        admin_product_delete.click_catalog_button()
        admin_product_delete.click_product_button()

    with allure.step("Выбор продукта для удаления"):
        admin_product_delete.click_checkbox_button()

    with allure.step("Нажатие кнопки удаления продукта"):
        delete_button = admin_product_delete.wait.until(
            EC.element_to_be_clickable(admin_product_delete.Delete_button),
            "Кнопка удаления не кликабельна",
        )
        delete_button.click()

    with allure.step("Подтверждение удаления продукта"):
        confirm_alert = WebDriverWait(browser, 5).until(
            EC.alert_is_present(), "Confirm алерт не появился"
        )
        confirm_alert.accept()
        time.sleep(1)

    with allure.step("Получение сообщения об успешном удалении продукта"):
        admin_product_delete.get_success_message(expected_text=expected_message)
