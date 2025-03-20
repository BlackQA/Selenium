from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import allure
import os


class CartPage:
    Cart_items = (By.XPATH, "//*[@id='checkout-total']/tr[1]/td[2]")
    Product_name = (By.XPATH, "//*[@id='shopping-cart']/div/table/tbody/tr/td[2]/a")

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

    @allure.step("Открытие страницы корзины")
    def open(self):
        cart_url = self.base_url + "/en-gb?route=checkout/cart"
        self.logger.info(f"Opening cart page: {cart_url}")
        self.browser.get(cart_url)

    @allure.step("Получение элементов товаров в корзине")
    def get_cart_items(self):
        self.logger.info("Getting cart items")
        return self.wait.until(EC.presence_of_all_elements_located(self.Cart_items))

    @allure.step("Получение названий товаров в корзине")
    def get_product_names(self):
        try:
            self.logger.info("Getting product names from cart")
            cart_items = self.wait.until(
                EC.presence_of_all_elements_located(self.Cart_items)
            )
            names = [item.find_element(*self.Product_name).text for item in cart_items]
            self.logger.info(f"Product names in cart: {names}")
            return names
        except Exception as e:
            self.logger.error(f"Error while getting product names from cart: {e}")
            raise Exception(f"Ошибка при получении названий товаров в корзине: {e}")
