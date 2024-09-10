from selenium.webdriver.common.by import By


class AsosSearchResultsPage:
    def __init__(self, driver):
        self.driver = driver

    def get_search_results(self):
        return self.driver.find_elements(By.XPATH, "//li[@class='product']")
