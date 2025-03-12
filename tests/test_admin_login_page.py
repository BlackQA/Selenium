from pages.login_admin_page import LoginAdminPage


def test_login_admin_page(browser, base_url):
    login_admin_page = LoginAdminPage(browser, base_url)
    login_admin_page.open()

    # Проверка наличия элемента username
    username_input = login_admin_page.get_username_input()
    assert (
        username_input.is_displayed()
    ), "Поле ввода имени пользователя не отображается"

    # Проверка наличия элемента password
    password_input = login_admin_page.get_password_input()
    assert password_input.is_displayed(), "Поле ввода пароля не отображается"

    # Проверка наличия элемента header
    header = login_admin_page.get_header()
    assert header.is_displayed(), "Заголовок страницы не отображается"

    # Проверка наличия элемента button_login
    button_login = login_admin_page.get_button_login()
    assert button_login.is_displayed(), "Кнопка 'Login' не отображается"

    # Проверка наличия элемента footer
    footer = login_admin_page.get_footer()
    assert footer.is_displayed(), "Футер не отображается"
