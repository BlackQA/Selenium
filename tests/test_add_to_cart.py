import pytest
import allure
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


@allure.feature("Корзина")
@allure.story("Добавление первого товара в корзину")
def test_add_first_product_to_cart(home_page, cart_page):
    with allure.step("Добавление первого товара в корзину"):
        added_product_name = home_page.add_first_product_to_cart()
        allure.attach(
            f"Добавленный товар: {added_product_name}",
            name="Добавленный товар",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Закрытие сообщения об успешном добавлении товара"):
        home_page.close_success_message_if_present()

    with allure.step("Переход в корзину"):
        home_page.get_cart_link()

    with allure.step("Получение списка товаров в корзине"):
        product_names = cart_page.get_product_names()
        allure.attach(
            "\n".join(product_names),
            name="Товары в корзине",
            attachment_type=allure.attachment_type.TEXT,
        )
    with allure.step(f"Проверка наличия товара '{added_product_name}' в корзине"):
        assert (
            added_product_name in product_names
        ), f"Добавленный товар '{added_product_name}' не найден в корзине"
