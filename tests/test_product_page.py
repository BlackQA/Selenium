from pages.product_page import ProductPage


def test_product_page(browser, base_url):
    product_page = ProductPage(browser, base_url)
    product_page.open()

    # Проверка наличия элемента image
    product_image = product_page.get_product_image()
    assert product_image.is_displayed(), "Изображение продукта не отображается"

    # Проверка наличия элемента price
    product_price = product_page.get_product_price()
    assert product_price.is_displayed(), "Цена продукта не отображается"

    # Проверка наличия элемента Add to Cart
    product_button_cart = product_page.get_product_button_cart()
    assert product_button_cart.is_displayed(), "Кнопка 'Add to Cart' не отображается"

    # Проверка наличия элемента title
    product_title = product_page.get_product_title()
    assert product_title.is_displayed(), "Заголовок продукта не отображается"

    # Проверка наличия элемента description
    product_description = product_page.get_product_description()
    assert product_description.is_displayed(), "Описание продукта не отображается"
