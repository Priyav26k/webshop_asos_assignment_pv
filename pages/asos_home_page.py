from selenium.webdriver.common.by import By


class AsosHomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_header(self):
        return self.driver.find_element(By.XPATH, "//header")

    def search_for_product(self, product_name):
        search_input = self.driver.find_element(By.XPATH, "//input[@id='search']")
        search_input.send_keys(product_name)
        search_input.submit()
