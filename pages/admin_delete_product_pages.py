from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import allure
import os


class AdminProductDelete:
    Username_input = (By.XPATH, "//*[@id='input-username']")
    Password_input = (By.XPATH, "//*[@id='input-password']")
    Button_login = (By.XPATH, "//*[@id='form-login']/div[3]/button")
    Catalog_button = (By.XPATH, "//*[@id='menu-catalog']/a")
    Product_button = (By.XPATH, "//*[@id='collapse-1']/li[2]/a")
    Checkbox_button = (By.XPATH, "//*[@id='form-product']/div[1]/table/tbody/tr[1]/td[1]/input")
    Delete_button = (By.XPATH, "//*[@id='content']/div[1]/div/div/button[3]")
    Alert = (By.XPATH, "//*[@id='alert']")

    def __init__(self, browser, base_url, to_file=True):
        self.browser = browser
        self.base_url = base_url
        self.wait = WebDriverWait(browser, 5)
        self.logger = logging.getLogger(self.__class__.__name__)
        os.makedirs("logs", exist_ok=True)
        if to_file:
            self.logger.addHandler(
                logging.FileHandler(f"logs/{self.browser.test_name}.log")
            )

    @allure.step("Открытие страницы администрирования")
    def open(self):
        catalog_url = self.base_url + "/administration"
        self.logger.info(f"Opening admin page: {catalog_url}")
        self.browser.get(catalog_url)

    @allure.step("Ввод имени пользователя: {username}")
    def enter_username(self, username):
        self.logger.info(f"Entering username: {username}")
        username_input = self.wait.until(
            EC.visibility_of_element_located(self.Username_input)
        )
        username_input.clear()
        username_input.send_keys(username)

    @allure.step("Ввод пароля: {password}")
    def enter_password(self, password):
        self.logger.info(f"Entering password: {password}")
        password_input = self.wait.until(
            EC.visibility_of_element_located(self.Password_input)
        )
        password_input.clear()
        password_input.send_keys(password)

    def _click(self, locator):
        self.logger.info(f"Clicking on element with locator: {locator}")
        button = self.wait.until(
            EC.element_to_be_clickable(locator),
            f"Элемент с локатором {locator} не кликабелен",
        )
        button.click()

    @allure.step("Нажатие кнопки входа в систему")
    def click_login_button(self):
        self._click(self.Button_login)

    @allure.step("Нажатие кнопки каталога")
    def click_catalog_button(self):
        self._click(self.Catalog_button)

    @allure.step("Нажатие кнопки продукта")
    def click_product_button(self):
        self._click(self.Product_button)

    @allure.step("Нажатие кнопки чекбокса для выбора товара")
    def click_checkbox_button(self):
        self._click(self.Checkbox_button)

    @allure.step("Нажатие кнопки удаления товара")
    def click_delete_button(self):
        self._click(self.Delete_button)

    @allure.step("Получение сообщения об успешном удалении товара")
    def get_success_message(self, expected_text="Success: You have modified products!"):
        self.logger.info(f"Checking for success message: {expected_text}")
        success_message = self.wait.until(
            EC.visibility_of_element_located(self.Alert),
            "Сообщение об успешном добавлении товара не появилось",
        )
        actual_text = success_message.text
        assert (
            expected_text in actual_text
        ), f"Текст сообщения не соответствует ожидаемому. Ожидалось: '{expected_text}', получили: '{actual_text}'"
        self.logger.info("Success message verified successfully")
