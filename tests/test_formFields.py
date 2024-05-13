from pages.formFields import FormFields
import pytest


@pytest.mark.xfail
def test_text_fields(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value('TEST')
    page.button_submit_click()
    assert page.alert_text == 'Message received!'


@pytest.mark.xfail
def test_text_fields_min(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value('T')
    page.button_submit_click()
    assert page.alert_text == 'Message received!'


@pytest.mark.xfail
def test_text_fields_empty(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value('')
    page.button_submit_click()
    assert page.alert_not_displayed


@pytest.mark.xfail
def test_text_fields_numbers(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value('12345')
    page.button_submit_click()
    assert page.alert_text == 'Message received!'


@pytest.mark.xfail
def test_text_fields_numbers_min(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value('1')
    page.button_submit_click()
    assert page.alert_text == 'Message received!'


@pytest.mark.xfail
def test_text_fields_symbols(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value('@')
    page.button_submit_click()
    assert page.alert_text == 'Message received!'


@pytest.mark.xfail
def test_text_fields_space_begin(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value(' asd')
    page.button_submit_click()
    assert page.alert_text == 'Message received!'


@pytest.mark.xfail
def test_text_fields_space_middle(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value('as d')
    page.button_submit_click()
    assert page.alert_text == 'Message received!'


@pytest.mark.xfail
def test_text_fields_space_end(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value('asd ')
    page.button_submit_click()
    assert page.alert_text == 'Message received!'


@pytest.mark.xfail
def test_text_fields_enter_keys(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value('abc' + '\n')
    assert page.alert_text == 'Message received!'


@pytest.mark.xfail
def test_text_fields_space_only(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value(' ' + '\n')
    assert page.alert_text == 'Message received!'
