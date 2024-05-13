from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


import pytest


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    service = Service(ChromeDriverManager(driver_version="124.0.6367.202").install(), chrome_options=options)
    chrome_browser = webdriver.Chrome(service=service)
    return chrome_browser
