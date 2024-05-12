from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.formFields import FormFields


def test_text_fields(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value('TEST')
    page.button_submit_click()
    assert page.alert_text == 'Message received!'
