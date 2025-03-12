from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementNotInteractableException,
)
import time


class HomePage:
    Product_list = (By.XPATH, "//*[@id='content']/div[2]/div[1]/div")
    Add_to_cart_button = (
        By.XPATH,
        "//*[@id='content']/div[2]/div[1]/div/div[2]/form/div/button[1]",
    )
    Cart_link = (By.XPATH, "//*[@id='top']/div/div[2]/ul/li[4]/a")
    Product_name = (By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/div/h4/a")
    Button_alert = (By.XPATH, "//*[@id='alert']/div/button")
    Success_message = (By.XPATH, "//*[@id='alert']")

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.wait = WebDriverWait(browser, 5)

    def open(self):
        self.browser.get(self.base_url)

    def get_product_elements(self):
        return self.wait.until(EC.presence_of_all_elements_located(self.Product_list))

    def get_first_product(self):
        products = self.get_product_elements()
        if not products:
            raise Exception("На странице нет товаров")
        return products[0]

    def add_first_product_to_cart(self):
        first_product = self.get_first_product()
        add_button = first_product.find_element(*self.Add_to_cart_button)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", add_button)
        time.sleep(0.5)
        add_button.click()
        product_name_element = first_product.find_element(*self.Product_name)
        product_name = product_name_element.text
        return product_name

    def close_success_message_if_present(self):
        try:
            success_message = self.wait.until(
                EC.visibility_of_element_located(self.Success_message),
                "Сообщение об успешном добавлении товара не появилось",
            )
            close_button = success_message.find_element(*self.Button_alert)
            close_button.click()
        except Exception:
            pass

    def get_cart_link(self):
        try:
            cart_button = self.wait.until(
                EC.element_to_be_clickable(self.Cart_link),
                "Ссылка на корзину не найдена или не кликабельна",
            )
            self.browser.execute_script(
                "arguments[0].scrollIntoView(true);", cart_button
            )
            time.sleep(0.5)
            self.wait.until(EC.visibility_of(cart_button))
            if not cart_button.is_displayed():
                raise Exception("Элемент найден, но не виден на странице.")
            try:
                cart_button.click()
            except Exception:
                self.browser.execute_script("arguments[0].click();", cart_button)
        except (
            TimeoutException,
            NoSuchElementException,
            ElementNotInteractableException,
        ) as e:
            raise Exception(f"Не удалось получить ссылку на корзину: {e}")
