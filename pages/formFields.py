from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Locators:
    BUTTON_SUBMIT_SELECTOR = (By.XPATH, '//*[@id="submit-btn"]')
    TEXT_FIELD_SELECTOR = (By.CSS_SELECTOR, '#name')


class FormFields(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        return self.browser.get('https://practice-automation.com/form-fields/')

    @property
    def button_submit(self):
        return self.find(Locators.BUTTON_SUBMIT_SELECTOR)

    @property
    def text_field(self):
        return self.find(Locators.TEXT_FIELD_SELECTOR)

    def button_submit_click(self):
        self.find(Locators.BUTTON_SUBMIT_SELECTOR, time=10).click()

    def text_field_value(self, word):
        self.text_field.send_keys(word)

    @property
    def alert_text(self):
        return self.browser.switch_to.alert.text
