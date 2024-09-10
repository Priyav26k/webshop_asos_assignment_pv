import unittest

from selenium.webdriver.chrome import webdriver

from pages.asos_home_page import AsosHomePage


class TestAsosHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.asos.com")
        self.home_page = AsosHomePage(self.driver)

    def test_title(self):
        self.assertEqual(self.home_page.get_title(), "ASOS | Online Shopping for the Latest Clothes & Fashion")

    def test_header(self):
        self.assertIsNotNone(self.home_page.get_header())

    def tearDown(self):
        self.driver.quit()
