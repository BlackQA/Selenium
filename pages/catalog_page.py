from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CatalogPage:
    Product_Compare = (By.XPATH, "//*[@id='compare-total']")
    Button_list = (By.XPATH, "//*[@id='button-list']")
    iPod_Classic_img = (By.XPATH, "//*[@id='product-list']/div[6]/div/div[1]/a/img")
    Pagination = (By.XPATH, "//*[@id='content']/div[5]/div[1]/ul")
    Add_to_Wish_List = (
        By.XPATH,
        "//*[@id='product-list']/div[7]/div/div[2]/form/div/button[2]",
    )

    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
        self.wait = WebDriverWait(browser, 5)

    def open(self):
        catalog_url = self.base_url + "/en-gb/catalog/desktops"
        self.browser.get(catalog_url)

    def get_product_compare(self):
        return self.wait.until(EC.visibility_of_element_located(self.Product_Compare))

    def get_button_list(self):
        return self.wait.until(EC.visibility_of_element_located(self.Button_list))

    def get_ipod_classic_img(self):
        return self.wait.until(EC.visibility_of_element_located(self.iPod_Classic_img))

    def get_pagination(self):
        return self.wait.until(EC.visibility_of_element_located(self.Pagination))

    def get_to_wish_list(self):
        return self.wait.until(EC.visibility_of_element_located(self.Add_to_Wish_List))
