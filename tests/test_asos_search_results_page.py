import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from pages.asos_search_results_page import AsosSearchResultsPage


class TestAsosSearchResultsPage(unittest.TestCase):
    def setUp(self):
        options = Options()  # Initialize Chrome options
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("https://www.asos.com/search?q=denim+jacket")
        self.search_results_page = AsosSearchResultsPage(self.driver)

    # def test_search_results(self):
    #     self.assertGreater(len(self.search_results_page.get_search_results()), 0)

    def tearDown(self):
        self.driver.quit()