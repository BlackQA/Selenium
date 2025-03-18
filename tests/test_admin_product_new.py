from pages.admin_product_new_pages import AdminProductNew
import pytest


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
    admin_product_new = AdminProductNew(browser, base_url)
    admin_product_new.open()

    admin_product_new.enter_username(username)
    admin_product_new.enter_password(password)
    admin_product_new.click_login_button()

    admin_product_new.click_catalog_button()
    admin_product_new.click_product_button()

    admin_product_new.add_product(product_name, meta_tag, model, seo_keyword)

    admin_product_new.get_success_message(expected_text=expected_message)
