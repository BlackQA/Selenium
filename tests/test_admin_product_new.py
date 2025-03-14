from pages.admin_product_new_pages import AdminProductNew


def test_add_new_product(browser, base_url):

    username = "user"
    password = "bitnami"

    product_name = "Новый Товар"
    meta_tag = "metateg"
    model = "MODEL123"
    seo_keyword = "seo_new_product"

    admin_product_new = AdminProductNew(browser, base_url)
    admin_product_new.open()

    try:
        admin_product_new.enter_username(username)
        admin_product_new.enter_password(password)
        admin_product_new.click_login_button()
    except Exception as e:
        assert False, f"Ошибка при входе в систему: {e}"

    try:
        admin_product_new.click_catalog_button()
        admin_product_new.click_product_button()
    except Exception as e:
        assert False, f"Ошибка при навигации к странице добавления товара: {e}"

    try:
        admin_product_new.click_add_new_button()
        admin_product_new.enter_product_name(product_name)
        admin_product_new.enter_meta_tag(meta_tag)
        admin_product_new.click_data_button()
        admin_product_new.enter_model_input(model)
        admin_product_new.click_seo_button()
        admin_product_new.enter_seo_input(seo_keyword)
        admin_product_new.click_save_button()
    except Exception as e:
        assert False, f"Ошибка при добавлении нового товара: {e}"

    try:
        admin_product_new.get_success_message(
            expected_text="Success: You have modified products!"
        )
    except Exception as e:
        assert False, f"Ошибка при проверке текста сообщения: {e}"
