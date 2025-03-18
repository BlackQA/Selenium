import pytest
from pages.currency_switch_home import SwitchHomePage


@pytest.fixture
def switch_home_page(browser, base_url):
    switch_home = SwitchHomePage(browser, base_url)
    switch_home.open()
    return switch_home


def test_currency_change_updates_prices(switch_home_page):
    currencies = ["EUR"]
    for currency in currencies:
        assert switch_home_page.check_currency_change(
            currency
        ), f"Цены не изменились при переключении на валюту '{currency}'"
