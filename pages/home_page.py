from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementNotInteractableException,
)
import time
import logging
import allure
import os


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

    @allure.step("Открытие домашней страницы")
    def open(self):
        self.logger.info(f"Opening home page: {self.base_url}")
        self.browser.get(self.base_url)

    @allure.step("Получение элементов товаров на странице")
    def get_product_elements(self):
        self.logger.info("Getting product elements")
        return self.wait.until(EC.presence_of_all_elements_located(self.Product_list))

    @allure.step("Получение первого товара на странице")
    def get_first_product(self):
        self.logger.info("Getting first product")
        products = self.get_product_elements()
        if not products:
            self.logger.error("No products found on the page")
            raise Exception("На странице нет товаров")
        return products[0]

    @allure.step("Добавление первого товара в корзину")
    def add_first_product_to_cart(self):
        self.logger.info("Adding first product to cart")
        first_product = self.get_first_product()
        add_button = first_product.find_element(*self.Add_to_cart_button)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", add_button)
        time.sleep(0.5)
        self.logger.info("Clicking on 'Add to Cart' button")
        add_button.click()
        product_name_element = first_product.find_element(*self.Product_name)
        product_name = product_name_element.text
        self.logger.info(f"Product '{product_name}' added to cart")
        return product_name

    @allure.step("Закрытие сообщения об успешном добавлении, если оно присутствует")
    def close_success_message_if_present(self):
        self.logger.info("Checking for success message")
        try:
            success_message = self.wait.until(
                EC.visibility_of_element_located(self.Success_message),
                "Сообщение об успешном добавлении товара не появилось",
            )
            close_button = success_message.find_element(*self.Button_alert)
            self.logger.info("Closing success message")
            close_button.click()
        except Exception:
            self.logger.info("No success message to close")
            pass

    @allure.step("Переход в корзину")
    def get_cart_link(self):
        self.logger.info("Getting cart link")
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
                self.logger.error("Cart link is present but not visible")
                raise Exception("Элемент найден, но не виден на странице.")
            self.logger.info("Clicking on cart link")
            try:
                cart_button.click()
            except Exception:
                self.logger.info("Using JavaScript to click on cart link")
                self.browser.execute_script("arguments[0].click();", cart_button)
        except (
            TimeoutException,
            NoSuchElementException,
            ElementNotInteractableException,
        ) as e:
            self.logger.error(f"Failed to get cart link: {e}")
            raise Exception(f"Не удалось получить ссылку на корзину: {e}")
