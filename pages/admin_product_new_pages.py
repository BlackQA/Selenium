from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdminProductNew:
    Username_input = (By.XPATH, "//*[@id='input-username']")
    Password_input = (By.XPATH, "//*[@id='input-password']")
    Button_login = (By.XPATH, "//*[@id='form-login']/div[3]/button")

    Catalog_button = (By.XPATH, "//*[@id='menu-catalog']/a")
    Product_button = (By.XPATH, "//*[@id='collapse-1']/li[2]/a")

    Add_new = (By.XPATH, "//*[@id='content']/div[1]/div/div/a")
    Name_input = (By.XPATH, "//*[@id='input-name-1']")
    Meta_input = (By.XPATH, "//*[@id='input-meta-title-1']")
    Data_button = (By.XPATH, "//*[@id='form-product']/ul/li[2]/a")
    Model_input = (By.XPATH, "//*[@id='input-model']")
    Seo_button = (By.XPATH, "//*[@id='form-product']/ul/li[11]/a")
    Seo_input = (By.XPATH, "//*[@id='input-keyword-0-1']")
    Save_button = (By.XPATH, "//*[@id='content']/div[1]/div/div/button")
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

    def click_login_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self.Button_login))
        button.click()

    def click_catalog_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self.Catalog_button))
        button.click()

    def click_product_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self.Product_button))
        button.click()

    def click_add_new_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self.Add_new))
        button.click()

    def enter_product_name(self, product_input):
        product_name = self.wait.until(
            EC.visibility_of_element_located(self.Name_input)
        )
        product_name.clear()
        product_name.send_keys(product_input)

    def enter_meta_tag(self, meta):
        meta_tag = self.wait.until(EC.visibility_of_element_located(self.Meta_input))
        meta_tag.clear()
        meta_tag.send_keys(meta)

    def click_data_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self.Data_button))
        button.click()

    def enter_model_input(self, model):
        model_input = self.wait.until(
            EC.visibility_of_element_located(self.Model_input)
        )
        model_input.clear()
        model_input.send_keys(model)

    def click_seo_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self.Seo_button))
        button.click()

    def enter_seo_input(self, seo):
        seo_input = self.wait.until(EC.visibility_of_element_located(self.Seo_input))
        seo_input.clear()
        seo_input.send_keys(seo)

    def click_save_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self.Save_button))
        button.click()

    def get_success_message(self, expected_text="Success: You have modified products!"):
        success_message = self.wait.until(
            EC.visibility_of_element_located(self.Alert),
            "Сообщение об успешном добавлении товара не появилось",
        )
        actual_text = success_message.text
        assert (
            expected_text in actual_text
        ), f"Текст сообщения не соответствует ожидаемому. Ожидалось: '{expected_text}', получили: '{actual_text}'"
