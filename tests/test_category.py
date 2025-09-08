def test_first_category(first_category):
    assert first_category.name == "Cмартфоны"
    assert first_category.description == "Телефоны на операционной системе Android"
    assert len(first_category.products) == 2

    assert first_category.category_count == 1
    assert first_category.product_count == 2
