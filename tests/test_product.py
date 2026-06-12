import pytest

from src.product import (BaseProduct, LawnGrass, PrintObject, Product,
                         Smartphone)


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


# тесты на инициализацию классов наследников
def test_Smartphone_init():
    smartphone = Smartphone(
        "Phone", "Description", 1000.0, 5, "Snapdragon", "Model X", 256, "Black"
    )

    assert smartphone.name == "Phone"
    assert smartphone.efficiency == "Snapdragon"
    assert smartphone.model == "Model X"
    assert smartphone.memory == 256
    assert smartphone.color == "Black"


def test_LawnGrass_init():
    grass = LawnGrass(
        "Японская поросль", "Description", 50.0, 100, "Japan", "20 дней", "Light Green"
    )

    assert grass.name == "Японская поросль"
    assert grass.country == "Japan"
    assert grass.germination_period == "20 дней"
    assert grass.color == "Light Green"


# сложение товаров одного класса
def test_add_same_class_products(product_1, product_2):
    result = product_1 + product_2
    expected = (42000.0 * 3) + (44000.0 * 5)
    assert result == expected


# сложение продукта с не продуктом
def test_add_with_non_product():
    product = Product("Товар", "Описание", 100.0, 10)

    result = product + "no product"
    assert result is None


def test_product_from_base_product():
    """Тест, что Product наследуется от BaseProduct"""
    assert issubclass(Product, BaseProduct)


def test_product_from_print_object():
    """Тест, что Product наследуется от PrintObject"""
    assert issubclass(Product, PrintObject)


def test_product_implements_all_abstract_methods():
    """Тест, что Product реализует все абстрактные методы BaseProduct"""
    product = Product("Test", "Desc", 100.0, 10)

    assert hasattr(product, "__init__")
    assert hasattr(product, "__str__")
    assert hasattr(product, "__add__")
    assert hasattr(product, "price")
    assert hasattr(Product, "new_product")


def test_super_in_constructors():
    """Тест, что super() правильно используется в конструкторах"""
    product = Product("Product", "Description", 100.0, 10)
    smartphone = Smartphone(
        "SmartPhone", "Description", 1000.0, 7, "Efficiency", "Model", 512, "Color"
    )
    grass = LawnGrass("Grass", "Description", 50.0, 100, "Country", "Period", "Color")

    assert product.name == "Product"
    assert smartphone.efficiency == "Efficiency"
    assert grass.country == "Country"


def test_product_zero_quantity_raises_value_error():
    """Тест на создание Product с quantity=0 вызывает ValueError"""
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Тестовый товар", "Описание", 1000.0, 0)


def test_product_negative_quantity_raises_value_error():
    """Тест: создание Product с отрицательным quantity вызывает ValueError"""
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Тестовый товар", "Описание", 1000.0, -5)


def test_new_product_zero_quantity_raises_value_error():
    """Тест: создание товара через new_product с quantity=0 вызывает ValueError"""
    products_data = {
        "name": "Тестовый товар",
        "description": "Описание",
        "price": 1000.0,
        "quantity": 0,
    }

    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product.new_product(products_data)
