# conftest.py
import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver():
    config = json.load(open("config/config.json"))
    browser = config["browser"]
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError("Unsupported browser")
    yield driver
    driver.quit()
