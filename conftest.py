from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


import pytest


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    service = Service(ChromeDriverManager(driver_version="124.0.6367.202").install())
    chrome_browser = webdriver.Chrome(service=service, options=options)
    return chrome_browser
