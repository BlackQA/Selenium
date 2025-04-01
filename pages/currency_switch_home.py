from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
import allure
import os


class SwitchHomePage:
    Currency_dropdown = (By.XPATH, "//*[@id='form-currency']/div/a")
    Currency_option = (By.XPATH, "//*[@id='form-currency']/div/ul/li[1]/a")
    Product_list = (By.XPATH, "//*[@id='content']/div[2]/div[1]/div")
    Product_price = (By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[2]/div/div/span[1]")

    def __init__(self, browser, base_url, to_file=True):
        self.browser = browser
        self.base_url = base_url
        self.wait = WebDriverWait(browser, 10)
        self.logger = logging.getLogger(self.__class__.__name__)
        os.makedirs("logs", exist_ok=True)
        if to_file:
            self.logger.addHandler(
                logging.FileHandler(f"logs/{self.browser.test_name}.log")
            )

    @allure.step("Открытие домашней страницы")
    def open(self):
        self.logger.info(f"Opening home page: {self.base_url}")
        self.browser.get(self.base_url)

    @allure.step("Получение элементов товаров на странице")
    def get_product_elements(self):
        self.logger.info("Getting product elements")
        return self.wait.until(
            EC.presence_of_all_elements_located(self.Product_list),
            "Товар не найден на странице",
        )

    @allure.step("Получение цен товаров")
    def get_product_prices(self):
        self.logger.info("Getting product elements")
        prices = []
        product_elements = self.get_product_elements()
        for product in product_elements:
            try:
                price_element = product.find_element(self.Product_price)
                prices.append(price_element.text)
                self.logger.info(f"Product price found: {price_element.text}")
            except Exception:
                self.logger.warning("No price found for a product, skipping")
                continue
        return prices

    @allure.step("Переключение валюты на: {currency_code}")
    def switch_currency(self, currency_code):
        self.logger.info(f"Switching currency to: {currency_code}")
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

    @allure.step("Проверка изменения цен после переключения валюты")
    def verify_prices_changed(self, original_prices):
        self.logger.info("Verifying if prices have changed")
        time.sleep(1)
        new_prices = self.get_product_prices()
        for original, new in zip(original_prices, new_prices):
            if original == new:
                self.logger.info("Price has not changed")
                return False
        self.logger.info("Prices have changed")
        return True

    @allure.step("Проверка изменения валюты на: {currency_code}")
    def check_currency_change(self, currency_code):
        self.logger.info(f"Checking currency change to: {currency_code}")
        original_prices = self.get_product_prices()
        self.switch_currency(currency_code)
        return self.verify_prices_changed(original_prices)
