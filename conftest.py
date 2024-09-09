import pytest
from utils.webdriver_factory import WebDriverFactory


@pytest.fixture(scope="function")
def driver():
    driver = WebDriverFactory.get_driver()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def home_page(driver):
    return WebDriverFactory.get_home_page(driver)


@pytest.fixture(scope="function")
def product_page(driver):
    return WebDriverFactory.get_product_page(driver)
