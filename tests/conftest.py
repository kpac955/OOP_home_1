import pytest


from src.product import Product
from src.category import Category

@pytest.fixture
def first_category():
    return Category(
        name = "Cмартфоны",
        description = "Телефоны на операционной системе Android",
        products = [
            Product("Samsung Galaxy S21", "128GB, Фиолетовый цвет, 64MP камера", 42000.0, 5),
            Product("Samsung Galaxy A18", "128GB, Белый цвет, 64MP камера", 45000.0, 7)
        ]
    )

@pytest.fixture
def product_1():
    return Product("Samsung Galaxy S21", "Смартфоны на Android", 42000.0, 3)

@pytest.fixture
def product_2():
    return Product("Iphone 11", "Смартфоны на IOS", 44000.0, 5)

