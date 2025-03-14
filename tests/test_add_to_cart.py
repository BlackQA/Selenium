import pytest
from pages.home_page import HomePage
from pages.cart_page import CartPage


@pytest.fixture
def home_page(browser, base_url):
    home = HomePage(browser, base_url)
    home.open()
    return home


@pytest.fixture
def cart_page(browser, base_url):
    cart = CartPage(browser, base_url)
    return cart


def test_add_first_product_to_cart(home_page, cart_page):
    added_product_name = None

    try:
        added_product_name = home_page.add_first_product_to_cart()
    except Exception as e:
        pytest.fail(f"Тест завершился с ошибкой: {e}")

    try:
        home_page.close_success_message_if_present()
    except Exception as e:
        pytest.fail(f"Не удалось закрыть alert: {e}")

    try:
        home_page.get_cart_link()
    except Exception as e:
        pytest.fail(f"Не удалось перейти в корзину: {e}")

    try:
        product_names = cart_page.get_product_names()
        assert (
            added_product_name in product_names
        ), f"Добавленный товар '{added_product_name}' не найден в корзине"
    except Exception as e:
        pytest.fail(f"Добавленный товар '{added_product_name}' не найден в корзине")
