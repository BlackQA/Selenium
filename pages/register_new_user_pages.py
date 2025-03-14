from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class RegisterNewUser:
    FirstName_input = (By.XPATH, "//*[@id='input-firstname']")
    LastName_input = (By.XPATH, "//*[@id='input-lastname']")
    Email_input = (By.XPATH, "//*[@id='input-email']")
    Password_input = (By.XPATH, "//*[@id='input-password']")
    Policy_checkbox = (By.XPATH, "//*[@id='form-register']/div/div/input")
    Continue_button = (By.XPATH, "//*[@id='form-register']/div/button")
    Text_created = (By.XPATH, "//*[@id='content']/h1")

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.wait = WebDriverWait(browser, 5)

    def open(self):
        catalog_url = self.base_url + "/en-gb?route=account/register"
        self.browser.get(catalog_url)

    def enter_first_name(self, first_name):
        username_input = self.wait.until(
            EC.visibility_of_element_located(self.FirstName_input)
        )
        username_input.clear()
        username_input.send_keys(first_name)

    def enter_last_name(self, last_name):
        lastname_input = self.wait.until(
            EC.visibility_of_element_located(self.LastName_input)
        )
        lastname_input.clear()
        lastname_input.send_keys(last_name)

    def enter_email(self, email):
        email_input = self.wait.until(
            EC.visibility_of_element_located(self.Email_input)
        )
        email_input.clear()
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.wait.until(
            EC.visibility_of_element_located(self.Password_input)
        )
        password_input.clear()
        password_input.send_keys(password)

    def click_checkbox_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self.Policy_checkbox))
        self.browser.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(0.5)
        button.click()

    def click_continue_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self.Continue_button))
        button.click()
        time.sleep(0.5)

    def get_message(self, expected_text="Your Account Has Been Created!"):
        message = self.wait.until(
            EC.visibility_of_element_located(self.Text_created),
            "Текс о создании нового пользователя не появился",
        )
        actual_text = message.text
        assert (
            expected_text in actual_text
        ), f"Текст сообщения не соответствует ожидаемому. Ожидалось: '{expected_text}', получили: '{actual_text}'"
