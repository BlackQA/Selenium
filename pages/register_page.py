from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage:
    Firstname_input = (By.XPATH, "//*[@id='input-firstname']")
    Lastname_input = (By.XPATH, "//*[@id='input-lastname']")
    Email_input = (By.XPATH, "//*[@id='input-email']")
    Password_input = (By.XPATH, "//*[@id='input-password']")
    Button_register = (By.XPATH, "//*[@id='form-register']/div/button")

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.wait = WebDriverWait(browser, 5)

    def open(self):
        catalog_url = self.base_url + "/en-gb?route=account/register"
        self.browser.get(catalog_url)

    def get_firstname_input(self):
        return self.wait.until(EC.visibility_of_element_located(self.Firstname_input))

    def get_lastname_input(self):
        return self.wait.until(EC.visibility_of_element_located(self.Lastname_input))

    def get_email_input(self):
        return self.wait.until(EC.visibility_of_element_located(self.Email_input))

    def get_password_input(self):
        return self.wait.until(EC.visibility_of_element_located(self.Password_input))

    def get_button_register(self):
        return self.wait.until(EC.element_to_be_clickable(self.Button_register))
