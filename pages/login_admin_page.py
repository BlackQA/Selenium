from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginAdminPage:
    Username_input = (By.XPATH, "//*[@id='input-username']")
    Password_input = (By.XPATH, "//*[@id='input-password']")
    Header = (By.XPATH, "//*[@id='content']/div/div/div/div/div[1]")
    Button_login = (By.XPATH, "//*[@id='form-login']/div[3]/button")
    Footer = (By.XPATH, "//*[@id='footer']/a")

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.wait = WebDriverWait(browser, 5)

    def open(self):
        catalog_url = self.base_url + "/administration"
        self.browser.get(catalog_url)

    def get_username_input(self):
        return self.wait.until(EC.visibility_of_element_located(self.Username_input))

    def get_password_input(self):
        return self.wait.until(EC.visibility_of_element_located(self.Password_input))

    def get_header(self):
        return self.wait.until(EC.visibility_of_element_located(self.Header))

    def get_button_login(self):
        return self.wait.until(EC.visibility_of_element_located(self.Button_login))

    def get_footer(self):
        return self.wait.until(EC.visibility_of_element_located(self.Footer))
