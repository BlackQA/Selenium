from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminProductDelete:
    Username_input = (By.XPATH, "//*[@id='input-username']")
    Password_input = (By.XPATH, "//*[@id='input-password']")
    Button_login = (By.XPATH, "//*[@id='form-login']/div[3]/button")
    Catalog_button = (By.XPATH, "//*[@id='menu-catalog']/a")
    Product_button = (By.XPATH, "//*[@id='collapse-1']/li[2]/a")
    Checkbox_button = (By.XPATH, "//*[@id='form-product']/div[1]/table/tbody/tr[1]/td[1]/input",)
    Delete_button = (By.XPATH, "//*[@id='content']/div[1]/div/div/button[3]")
    Alert = (By.XPATH, "//*[@id='alert']")

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.wait = WebDriverWait(browser, 5)

    def open(self):
        catalog_url = self.base_url + "/administration"
        self.browser.get(catalog_url)

    def enter_username(self, username):
        username_input = self.wait.until(
            EC.visibility_of_element_located(self.Username_input)
        )
        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.wait.until(
            EC.visibility_of_element_located(self.Password_input)
        )
        password_input.clear()
        password_input.send_keys(password)

    def _click(self, locator):
        button = self.wait.until(
            EC.element_to_be_clickable(locator),
            f"Элемент с локатором {locator} не кликабелен",
        )
        button.click()

    def click_login_button(self):
        self._click(self.Button_login)

    def click_catalog_button(self):
        self._click(self.Catalog_button)

    def click_product_button(self):
        self._click(self.Product_button)

    def click_checkbox_button(self):
        self._click(self.Checkbox_button)

    def click_delete_button(self):
        self._click(self.Delete_button)

    def get_success_message(self, expected_text="Success: You have modified products!"):
        success_message = self.wait.until(
            EC.visibility_of_element_located(self.Alert),
            "Сообщение об успешном добавлении товара не появилось",
        )
        actual_text = success_message.text
        assert (
            expected_text in actual_text
        ), f"Текст сообщения не соответствует ожидаемому. Ожидалось: '{expected_text}', получили: '{actual_text}'"
