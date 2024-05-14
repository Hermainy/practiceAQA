from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Locators:
    BUTTON_SUBMIT_SELECTOR = (By.ID, 'submit-btn')
    TEXT_FIELD_SELECTOR = (By.ID, 'name')

    def DRINK_SELECTOR(self, option):
        return By.XPATH, "//input[@value='" + option + "']"

    ALL_CHECKBOXES_SELECTOR = (By.CSS_SELECTOR, 'input[type="checkbox"]')


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

    @property
    def alert_not_displayed(self):
        return self.not_alert_present()

    def submit_by_enter(self):
        self.browser.send_keys(Keys.ENTER)

    def check_checkbox(self, option):
        self.find(Locators.DRINK_SELECTOR(self.browser, option)).click()

    def checkbox_value(self, option):
        return self.find(Locators.DRINK_SELECTOR(self.browser, option)).is_selected()

    def check_all_checkboxes(self):
        all_list = self.finds(Locators.ALL_CHECKBOXES_SELECTOR)
        for element in all_list:
            element.click()

    def all_checkbox_value(self) -> bool:
        all_list = self.finds(Locators.ALL_CHECKBOXES_SELECTOR)
        return all([element.is_selected() for element in all_list])
