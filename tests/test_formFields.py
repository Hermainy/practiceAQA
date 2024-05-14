import time

from pages.formFields import FormFields
import pytest


@pytest.mark.xfail
@pytest.mark.regress
def test_text_fields(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value('TEST')
    page.button_submit_click()
    assert page.alert_text == 'Message received!'


@pytest.mark.xfail
@pytest.mark.regress
def test_text_fields_min(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value('T')
    page.button_submit_click()
    assert page.alert_text == 'Message received!'


@pytest.mark.xfail
@pytest.mark.regress
def test_text_fields_empty(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value('')
    page.button_submit_click()
    assert page.alert_not_displayed


@pytest.mark.xfail
@pytest.mark.regress
def test_text_fields_numbers(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value('12345')
    page.button_submit_click()
    assert page.alert_text == 'Message received!'


@pytest.mark.xfail
@pytest.mark.regress
def test_text_fields_numbers_min(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value('1')
    page.button_submit_click()
    assert page.alert_text == 'Message received!'


@pytest.mark.xfail
@pytest.mark.regress
def test_text_fields_symbols(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value('@')
    page.button_submit_click()
    assert page.alert_text == 'Message received!'


@pytest.mark.xfail
@pytest.mark.regress
def test_text_fields_space_begin(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value(' asd')
    page.button_submit_click()
    assert page.alert_text == 'Message received!'


@pytest.mark.xfail
@pytest.mark.regress
def test_text_fields_space_middle(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value('as d')
    page.button_submit_click()
    assert page.alert_text == 'Message received!'


@pytest.mark.xfail
@pytest.mark.regress
def test_text_fields_space_end(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value('asd ')
    page.button_submit_click()
    assert page.alert_text == 'Message received!'


@pytest.mark.regress
def test_text_fields_enter_keys(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value('abc' + '\n')
    assert page.alert_text == 'Message received!'


@pytest.mark.regress
def test_text_fields_space_only(browser):
    page = FormFields(browser)
    page.open()
    page.text_field_value(' ' + '\n')
    assert page.alert_text == 'Message received!'


@pytest.mark.regress
def test_checkbox_Water(browser):
    page = FormFields(browser)
    page.open()
    page.check_checkbox('Water')
    assert page.checkbox_value('Water')


@pytest.mark.regress
def test_checkbox_Milk(browser):
    page = FormFields(browser)
    page.open()
    page.check_checkbox('Milk')
    assert page.checkbox_value('Milk')


@pytest.mark.regress
def test_checkbox_Coffee(browser):
    page = FormFields(browser)
    page.open()
    page.check_checkbox('Coffee')
    assert page.checkbox_value('Coffee')


@pytest.mark.regress
def test_checkbox_Wine(browser):
    page = FormFields(browser)
    page.open()
    page.check_checkbox('Wine')
    assert page.checkbox_value('Wine')


@pytest.mark.regress
def test_checkbox_Ctrl_Alt_Delight(browser):
    page = FormFields(browser)
    page.open()
    page.check_checkbox('Ctrl-Alt-Delight')
    assert page.checkbox_value('Ctrl-Alt-Delight')


@pytest.mark.regress
def test_all_checkboxes(browser):
    page = FormFields(browser)
    page.open()
    page.check_all_checkboxes()
    assert page.all_checkbox_value() == True
