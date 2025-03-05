from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LogoutAdminPages:
    Username_input = (By.XPATH, "//*[@id='input-username']")
    Password_input = (By.XPATH, "//*[@id='input-password']")
    Button_login = (By.XPATH, "//*[@id='form-login']/div[3]/button")
    Button_logout = (By.XPATH, "//*[@id='nav-logout']/a")

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

    def click_login_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self.Button_login))
        button.click()

    def get_logout_button(self):
        return self.wait.until(EC.visibility_of_element_located(self.Button_logout))

    def logout(self):
        logout_button = self.get_logout_button()
        logout_button.click()

    def get_login_button_after_logout(self):
        return self.wait.until(EC.visibility_of_element_located(self.Button_login))

    def get_title(self):
        return self.browser.title
