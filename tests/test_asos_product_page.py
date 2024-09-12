import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from pages.asos_product_page import AsosProductPage


class TestAsosProductPage(unittest.TestCase):
    def setUp(self):
        options = Options()  # Initialize Chrome options
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("https://www.asos.com/asos-design/asos-design-oversized-denim-jacket/prd/13451113")
        self.product_page = AsosProductPage(self.driver)

    def test_product_name(self):
        self.assertEqual(self.product_page.get_product_name(), "ASOS DESIGN Oversized Denim Jacket")

    def test_product_price(self):
        self.assertIsNotNone(self.product_page.get_product_price())

    def tearDown(self):
        self.driver.quit()
