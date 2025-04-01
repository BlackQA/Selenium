from pages.register_new_user_pages import RegisterNewUser
import pytest
import allure


@pytest.mark.parametrize(
    "first_name, last_name, email, password, expected_message",
    [
        (
            "John",
            "Connor",
            "sirijit223@doishy.com",
            "12345",
            "Your Account Has Been Created!",
        )
    ],
)
def test_register_new_user(
    browser, base_url, first_name, last_name, email, password, expected_message
):

    with allure.step("Открытие страницы регистрации"):
        register_user = RegisterNewUser(browser, base_url)
        register_user.open()

    with allure.step("Ввод имени"):
        register_user.enter_first_name(first_name)

    with allure.step("Ввод фамилии"):
        register_user.enter_last_name(last_name)

    with allure.step("Ввод email"):
        register_user.enter_email(email)

    with allure.step("Ввод пароля"):
        register_user.enter_password(password)

    with allure.step("Принятие политики конфиденциальности"):
        register_user.click_checkbox_button()

    with allure.step("Нажатие кнопки продолжения"):
        register_user.click_continue_button()

    with allure.step("Проверка сообщения об успешной регистрации"):
        register_user.get_message(expected_text=expected_message)
