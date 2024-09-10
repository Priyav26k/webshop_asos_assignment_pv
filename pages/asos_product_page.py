from selenium.webdriver.common.by import By


class AsosProductPage:
    def __init__(self, driver):
        self.driver = driver

    def get_product_name(self):
        return self.driver.find_element(By.XPATH, "//h1[@itemprop='name']").text

    def get_product_price(self):
        return self.driver.find_element(By.XPATH, "//span[@itemprop='price']").text
