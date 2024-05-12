from pages.popups import Popups


def test_alert_popup_button(browser):
    page = Popups(browser)
    page.open()
    page.button_alert_click()
    assert page.alert_text == 'Hi there, pal!'
