from pages.register_page import RegisterPage


def test_register_page(browser, base_url):
    register_page = RegisterPage(browser, base_url)
    register_page.open()

    # Проверка наличия элемент firstname_input
    firstname_input = register_page.get_firstname_input()
    assert firstname_input.is_displayed(), "Поле ввода имени не отображается"

    # Проверка наличия элемент lastname_input
    lastname_input = register_page.get_lastname_input()
    assert lastname_input.is_displayed(), "Поле ввода фамилии не отображается"

    # Проверка наличия элемент email_input
    email_input = register_page.get_email_input()
    assert email_input.is_displayed(), "Поле ввода email не отображается"

    # Проверка наличия элемент password_input
    password_input = register_page.get_password_input()
    assert password_input.is_displayed(), "Поле ввода пароля не отображается"

    # Проверка наличия элемент  button_register
    button_register = register_page.get_button_register()
    assert button_register.is_displayed(), "Кнопка 'Continue' не отображается"
