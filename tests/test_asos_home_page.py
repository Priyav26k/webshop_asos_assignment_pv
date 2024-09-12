import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from pages.asos_home_page import AsosHomePage


class TestAsosHomePage(unittest.TestCase):
    def setUp(self):
        options = Options()  # Initialize Chrome options
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("https://www.asos.com")
        self.home_page = AsosHomePage(self.driver)

    def test_title(self):
        self.assertEqual(self.home_page.get_title(), "ASOS | Online Shopping for the Latest Clothes & Fashion")

    def test_header(self):
        self.assertIsNotNone(self.home_page.get_header())

    def tearDown(self):
        self.driver.quit()
