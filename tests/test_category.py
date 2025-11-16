import pytest

from src.category import Category, Product


def test_first_category(first_category):
    assert first_category.name == "Cмартфоны"
    assert first_category.description == "Телефоны на операционной системе Android"
    products_list = first_category.products.split("\n")
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


def test_str_category(first_category):
    """Тест __str__ метода"""
    result = str(first_category)

    assert "Cмартфоны" in result

    # Проверяем, что строка содержит правильное общее количество товаров
    assert "количество продуктов: 12 шт." in result

    # Проверяем соответствие формату
    assert result == "Cмартфоны, количество продуктов: 12 шт."


def test_add_regular_product_to_category():

    category = Category("Тест", "Категория")
    product = Product("Обычный товар", "Описание", 100.0, 10)

    category.add_product(product)

    assert "Обычный товар" in category.products


def test_cannot_add_string_to_category():
    category = Category("Тест", "Категория")

    with pytest.raises(TypeError):
        category.add_product("просто строка")


def test_average_price_with_existing_products(first_category):
    """Тест: average_price возвращает правильную среднюю цену для категории с товарами"""
    average = first_category.average_price()
    expected = (42000.0 + 45000.0) / 2  # Среднее двух товаров в фикстуре
    assert average == expected


def test_average_price_empty_category_returns_zero():
    """Тест: average_price возвращает 0 для пустой категории"""
    empty_category = Category("Пустая", "Категория без товаров")
    assert empty_category.average_price() == 0


def test_average_price_single_product_returns_its_price():
    """Тест: average_price для категории с одним товаром возвращает его цену"""
    category = Category("Один товар", "Категория")
    product = Product("Товар", "Описание", 2500.0, 10)
    category.add_product(product)

    assert category.average_price() == 2500.0
