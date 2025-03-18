from pages.register_new_user_pages import RegisterNewUser
import pytest


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

    register_new_user = RegisterNewUser(browser, base_url)
    register_new_user.open()

    register_new_user.enter_first_name(first_name)
    register_new_user.enter_last_name(last_name)
    register_new_user.enter_email(email)
    register_new_user.enter_password(password)

    register_new_user.click_checkbox_button()
    register_new_user.click_continue_button()

    register_new_user.get_message(expected_text=expected_message)
