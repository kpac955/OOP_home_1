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
            Product("Iphone 11", "128GB, Белый цвет, 64MP камера", 45000.0, 7)
        ]
    )

@pytest.fixture
def second_category():
    return Category(
        name = "Телевизоры",
        description = "Телевизоры 4K",
        products = [
            Product("Samsung LXN00055", "4К, Wi-fi, 3HDMI d55 ", 55000.0, 8),
            Product("LG XU2345N", "4K, Wi-fi, USB port, LAN port", 53000.0, 7)
        ]
    )

@pytest.fixture
def product_1():
    return Product("Samsung Galaxy S21", "Смартфоны на Android", 42000.0, 3)

@pytest.fixture
def product_2():
    return Product("Iphone 11", "Смартфоны на IOS", 44000.0, 5)

