from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    Product_img = (By.XPATH, "//*[@id='content']/div[1]/div[1]/div/a/img")
    Product_price = (By.XPATH, "//*[@id='content']/div[1]/div[2]/ul[2]/li[1]/h2/span")
    Product_button_cart = (By.XPATH, "//*[@id='button-cart']")
    Product_title = (By.XPATH, "//*[@id='content']/div[1]/div[2]/h1")
    Product_description = (By.XPATH, "//*[@id='tab-description']/p")

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.wait = WebDriverWait(browser, 5)

    def open(self):
        catalog_url = self.base_url + "/en-gb/product/iphone"
        self.browser.get(catalog_url)

    def get_product_image(self):
        return self.wait.until(EC.visibility_of_element_located(self.Product_img))

    def get_product_price(self):
        return self.wait.until(EC.visibility_of_element_located(self.Product_price))

    def get_product_button_cart(self):
        return self.wait.until(EC.element_to_be_clickable(self.Product_button_cart))

    def get_product_title(self):
        return self.wait.until(EC.visibility_of_element_located(self.Product_title))

    def get_product_description(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.Product_description)
        )
