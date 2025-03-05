from pages import CatalogPage


def test_catalog_page(browser, base_url):
    catalog_page = CatalogPage(browser, base_url)
    catalog_page.open()

    # Проверка наличия элемента "Product Compare"
    product_compare = catalog_page.get_product_compare()
    assert product_compare.is_displayed(), "Элемент 'Product Compare' не отображается"

    # Проверка наличия элемента "List"
    button_list = catalog_page.get_button_list()
    assert button_list.is_displayed(), "Элемент 'List' не отображается"

    # Проверка наличия изображения iPod Classic
    ipod_classic_img = catalog_page.get_ipod_classic_img()
    assert ipod_classic_img.is_displayed(), "Изображение iPod Classic не отображается"

    # Проверка наличия пагинации
    pagination = catalog_page.get_pagination()
    assert pagination.is_displayed(), "Пагинация не отображается"

    # Проверка наличия элемента "add_to_wish_list"
    add_to_wish_list = catalog_page.get_to_wish_list()
    assert add_to_wish_list.is_displayed(), "Элемент 'add_to_wish_list' не отображается"
