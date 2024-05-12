from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Locators:
    BUTTON_ALERT_SELECTOR = (By.XPATH, '//*[@id="alert"]')


class Popups(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        return self.browser.get('https://practice-automation.com/popups/')

    @property
    def button_alert(self):
        return self.find(Locators.BUTTON_ALERT_SELECTOR)

    def button_alert_click(self):
        self.find(Locators.BUTTON_ALERT_SELECTOR, time=5).click()

    @property
    def alert_text(self):
        return self.browser.switch_to.alert.text
