from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    Cart_items = (By.XPATH, "//*[@id='checkout-total']/tr[1]/td[2]")
    Product_name = (By.XPATH, "//*[@id='shopping-cart']/div/table/tbody/tr/td[2]/a")

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.wait = WebDriverWait(browser, 5)

    def open(self, base_url):
        self.browser.get(base_url + "/en-gb?route=checkout/cart")

    def get_cart_items(self):
        return self.wait.until(EC.presence_of_all_elements_located(self.Cart_items))

    def get_product_names(self):
        try:
            cart_items = self.wait.until(
                EC.presence_of_all_elements_located(self.Cart_items)
            )
            names = [item.find_element(*self.Product_name).text for item in cart_items]
            return names
        except Exception as e:
            raise Exception(f"Ошибка при получении названий товаров в корзине: {e}")
