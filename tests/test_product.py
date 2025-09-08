def test_product_1_init(product_1):
    assert product_1.name == "Samsung Galaxy S21"
    assert product_1.description == "Смартфоны на Android"
    assert product_1.price == 42000.0
    assert product_1.quantity == 3


def test_product_2_init(product_2):
    assert product_2.name == "Iphone 11"
    assert product_2.description == "Смартфоны на IOS"
    assert product_2.price == 44000.0
    assert product_2.quantity == 5
