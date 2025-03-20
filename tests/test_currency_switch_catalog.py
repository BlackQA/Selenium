import pytest
from pages.currency_switch_catalog import SwitchCatalogPage
import allure


@pytest.fixture
def switch_home_page(browser, base_url):
    switch_home = SwitchCatalogPage(browser, base_url)
    switch_home.open()
    return switch_home


@allure.feature("Переключение валюты")
@allure.story("Проверка изменения цен при переключении валюты")
@pytest.mark.parametrize("currency", ["EUR"])
def test_currency_change_updates_prices(switch_home_page, currency):
    with allure.step(f"Проверка изменения цен при переключении валюты на '{currency}'"):
        assert switch_home_page.check_currency_change(
            currency
        ), f"Цены не изменились при переключении на валюту '{currency}'"
