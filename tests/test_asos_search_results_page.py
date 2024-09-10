import unittest

from selenium.webdriver.chrome import webdriver

from pages.asos_search_results_page import AsosSearchResultsPage


class TestAsosSearchResultsPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.asos.com/search?q=denim+jacket")
        self.search_results_page = AsosSearchResultsPage(self.driver)

    def test_search_results(self):
        self.assertGreater(len(self.search_results_page.get_search_results()), 0)

    def tearDown(self):
        self.driver.quit()
