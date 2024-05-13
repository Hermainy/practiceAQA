from selenium import webdriver
from selenium.webdriver.chrome.options import Options


import pytest


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_browser = webdriver.Chrome(options=options)
    return chrome_browser
