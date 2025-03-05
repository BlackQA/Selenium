from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    Logo = (By.XPATH, "//*[@id='logo']/a/img")
    Header = (By.XPATH, "//*[@id='top']/div/div[2]/ul/li[4]/a/span")
    Search_bar = (By.XPATH, "//*[@id='search']/input")
    Menu = (By.XPATH, "//*[@id='narbar-menu']")
    Product_featured = (By.XPATH, "//*[@id='content']/div[2]/div[1]/div/div[1]/a/img")

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 5)

    def get_logo(self):
        return self.wait.until(EC.visibility_of_element_located(self.Logo))

    def get_header(self):
        return self.wait.until(EC.visibility_of_element_located(self.Header))

    def get_search_bar(self):
        return self.wait.until(EC.visibility_of_element_located(self.Search_bar))

    def get_menu(self):
        return self.wait.until(EC.visibility_of_element_located(self.Menu))

    def get_product_featured(self):
        return self.wait.until(EC.visibility_of_element_located(self.Product_featured))
