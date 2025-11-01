from src.product import Product


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


def test_price_getter_setter(product_1):
    """Тест геттера и сеттера цены"""
    # Через геттер проверяем исходную цену
    assert product_1.price == 42000.0

    # Через сеттер устанавливаем новую цену
    product_1.price = 45000.0
    assert product_1.price == 45000.0

    # Пытаемся установить недопустимую цену
    product_1.price = -1000.0
    assert product_1.price == 45000.0

    # Пытаемся установить нулевую цену
    product_1.price = 0
    assert product_1.price == 45000.0


def test_new_product_creation():
    """Тест нового товара через класс-метод"""
    products_data = {
        "name": "Xiaomi Redmi Note",
        "description": "Бюджетный смартфон",
        "price": 25000.0,
        "quantity": 7,
    }

    # Создаем товар с помощью класс-метода new_product
    new_product = Product.new_product(products_data)

    # Проверяем, что товар создан с правильными параметрами
    assert new_product.name == "Xiaomi Redmi Note"
    assert new_product.description == "Бюджетный смартфон"
    assert new_product.price == 25000.0
    assert new_product.quantity == 7


def test_str_product(product_1, product_2):
    assert "Samsung Galaxy S21" in str(product_1)
    assert "42000.0" in str(product_1)
    assert "3" in str(product_1)
    assert "руб." in str(product_1)
    assert "Остаток:" in str(product_1)
    assert "шт." in str(product_1)

def test_add_product(product_1, product_2):
    result = product_1 + product_2

    # Проверка на то, что результат - число
    assert isinstance(result, (int, float))

    # Проверяем правильность вычислений
    expected = (42000.0 * 3) + (44000.0 * 5)
    assert result == expected
    assert result == 346000.0
