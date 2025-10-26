def test_first_category(first_category):
    assert first_category.name == "Cмартфоны"
    assert first_category.description == "Телефоны на операционной системе Android"
    products_list = first_category.products.split('\n')
    assert len(products_list) == 2


def test_add_product_to_category(first_category, product_1):
    initial_products_count = (
        len(first_category.products.split("\n")) if first_category.products else 0
    )

    first_category.add_product(product_1)

    products_output = first_category.products
    assert product_1.name in products_output

    new_products_count = len(products_output.split("\n")) if products_output else 0
    assert new_products_count == initial_products_count + 1


def test_products_property_content(first_category):
    products_output = first_category.products

    assert "Samsung Galaxy S21" in products_output
    assert "Samsung Galaxy A18" in products_output

    assert "42000" in products_output
    assert "45000" in products_output

    assert "5" in products_output
    assert "7" in products_output
