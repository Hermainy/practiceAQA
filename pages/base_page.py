from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args, time=10):
        return WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(args),
                                                       message=f"Can't find element by locator {args}")
