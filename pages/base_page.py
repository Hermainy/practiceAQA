from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, args, time=10):
        return WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(args),
                                                       message=f"Can't find element by locator {args}")

    def finds(self, args, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(args),
                                                       message=f"Can't find elements by locator {args}")

    def not_alert_present(self, time=2):
        try:
            WebDriverWait(self.browser, time).until(EC.alert_is_present())
        except TimeoutException:
            return True
