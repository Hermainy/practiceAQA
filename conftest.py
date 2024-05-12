from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import pytest


@pytest.fixture()
def browser():
    service = Service(ChromeDriverManager(driver_version="124.0.6367.202").install())
    chrome_browser = webdriver.Chrome(service=service)
    return chrome_browser
