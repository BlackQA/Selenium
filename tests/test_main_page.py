from pages import MainPage


def test_main_page(browser):
    browser.get(browser.url)
    main_page = MainPage(browser)

    # Проверка наличия логотипа
    logo = main_page.get_logo()
    assert logo.is_displayed(), "Логотип не отображается"

    # Проверка наличия заголовка корзины
    header = main_page.get_header()
    assert header.is_displayed(), "Заголовок корзины не отображается"

    # Проверка наличия строки поиска
    search_bar = main_page.get_search_bar()
    assert search_bar.is_displayed(), "Строка поиска не отображается"

    # Проверка наличия меню
    menu = main_page.get_menu()
    assert menu.is_displayed(), "Меню не отображается"

    # Проверка наличия рекомендованного продукта
    product_featured = main_page.get_product_featured()
    assert product_featured.is_displayed(), "Рекомендованный продукт не отображается"
