from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class SwitchCatalogPage:
    Currency_dropdown = (By.XPATH, "//*[@id='form-currency']/div/a")
    Currency_option = (By.XPATH, "//*[@id='form-currency']/div/ul/li[1]/a")
    Product_list = (By.XPATH, "//*[@id='product-list']/div[2]/div")
    Product_price = (
        By.XPATH,
        "//*[@id='product-list']/div[2]/div/div[2]/div/div/span[1]",
    )

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.wait = WebDriverWait(browser, 5)

    def open(self):
        catalog_url = self.base_url + "/en-gb/catalog/desktops"
        self.browser.get(catalog_url)

    def get_product_elements(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(self.Product_list),
            "Товар не найден на странице",
        )

    def get_product_prices(self):
        prices = []
        product_elements = self.get_product_elements()
        for product in product_elements:
            try:
                price_element = product.find_element(self.Product_price)
                prices.append(price_element.text)
            except Exception:
                continue
        return prices

    def switch_currency(self, currency_code):
        dropdown = self.wait.until(
            EC.element_to_be_clickable(self.Currency_dropdown),
            "Выпадающий список валюты не найден или не кликабелен",
        )
        dropdown.click()
        option = self.wait.until(
            EC.element_to_be_clickable(self.Currency_option),
            f"Опция валюты '{currency_code}' не найдена или не кликабельна",
        )
        option.click()

    def verify_prices_changed(self, original_prices):
        time.sleep(1)
        new_prices = self.get_product_prices()
        for original, new in zip(original_prices, new_prices):
            if original == new:
                return False
        return True

    def check_currency_change(self, currency_code):
        original_prices = self.get_product_prices()
        self.switch_currency(currency_code)
        return self.verify_prices_changed(original_prices)
