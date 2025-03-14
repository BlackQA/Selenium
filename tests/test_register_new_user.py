from pages.register_new_user_pages import RegisterNewUser


def test_register_new_user(browser, base_url):

    first_name = "John"
    last_name = "Connor"
    email = "sirijit223@doishy.com"
    password = "12345"

    register_new_user = RegisterNewUser(browser, base_url)
    register_new_user.open()

    try:
        register_new_user.enter_first_name(first_name)
        register_new_user.enter_last_name(last_name)
        register_new_user.enter_email(email)
        register_new_user.enter_password(password)
    except Exception as e:
        assert False, f"Ошибка при регистрации: {e}"

    try:
        register_new_user.click_checkbox_button()
        register_new_user.click_continue_button()
    except Exception as e:
        assert False, f"Ошибка при нажатии кнопки регистрации: {e}"

    try:
        register_new_user.get_message(expected_text="Your Account Has Been Created!")
    except Exception as e:
        assert False, f"Ошибка при проверке текста сообщения: {e}"
