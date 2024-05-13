from pages.formFields import FormFields
import pytest


@pytest.mark.skip
@pytest.mark.regress
def test_text_fields(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value('TEST')
    page.button_submit_click()
    assert page.alert_text == 'Message received!'
