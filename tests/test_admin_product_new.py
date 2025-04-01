from pages.admin_product_new_pages import AdminProductNew
import pytest
import allure


@pytest.mark.parametrize(
    "username, password, product_name, meta_tag, model, seo_keyword, expected_message",
    [
        (
            "user",
            "bitnami",
            "Новый Товар 1",
            "Мета-тег для нового товара 1",
            "MODEL123",
            "seo_new_product_1",
            "Success: You have modified products!",
        )
    ],
)
def test_add_new_product(
    browser,
    base_url,
    username,
    password,
    product_name,
    meta_tag,
    model,
    seo_keyword,
    expected_message,
):
    with allure.step("Создание экземпляра AdminProductNew"):
        admin_product_new = AdminProductNew(browser, base_url)
    with allure.step("Открытие страницы администрирования"):
        admin_product_new.open()
    with allure.step("Вход в систему"):
        admin_product_new.enter_username(username)
        admin_product_new.enter_password(password)
        admin_product_new.click_login_button()
    with allure.step("Навигация к разделу каталога и продуктам"):
        admin_product_new.click_catalog_button()
        admin_product_new.click_product_button()
    with allure.step("Добавление нового продукта"):
        admin_product_new.add_product(product_name, meta_tag, model, seo_keyword)
    with allure.step("Проверка сообщения об успешном добавлении продукта"):
        admin_product_new.get_success_message(expected_text=expected_message)
