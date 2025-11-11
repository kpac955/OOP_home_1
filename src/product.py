from abc import ABC, abstractmethod


class PrintObject:
    """Миксин для логирования создания объектов"""

    def __init__(self, *args, **kwargs):
        # Вызываем конструктор следующего класса в цепочке наследования
        super().__init__(*args, **kwargs)
        print(f"Создан объект: {self.__repr__()}")

    def __repr__(self):
        class_name = self.__class__.__name__
        attributes = []
        for key, value in self.__dict__.items():
            if not key.startswith("_"):
                attributes.append(f"{key}={repr(value)}")
        return f"{class_name}({', '.join(attributes)})"


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов"""

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @property
    @abstractmethod
    def price(self):
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, products_data, products_list=None):
        pass


class Product(PrintObject, BaseProduct):
    name: str
    description: str
    price: float
    quantity: int
    product_count = 0

    def __init__(self, name, description, price, quantity):
        # Инициализируем атрибуты
        self.name = name
        self.description = description
        self.__price = float(price)
        self.quantity = int(quantity)

        # Вызов конструктора миксина и BaseProduct
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            return
        if type(self) is not type(other):
            raise TypeError(
                "Можно складывать товары только из одинаковых классов продуктов"
            )
        return (self.price * self.quantity) + (other.price * other.quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        new_price = float(new_price)
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, products_data, products_list=None):
        """Класс метод, принимающий на вход параметры товара в словаре
        и возвращает созданный объект класса, также добавлен второй аргумент 'products_list'
        для проверки дубликатов"""
        if products_list is None:
            products_list = []

        name = products_data["name"]
        description = products_data["description"]
        price = products_data["price"]
        quantity = products_data["quantity"]

        for same_product in products_list:
            if same_product.name == name:
                same_product.quantity += quantity
                same_product.price = max(same_product.price, price)
                print(f"Товар {name} существует " f"Цена и количество обновлены")
                return same_product

        return cls(name, description, price, quantity)


class Smartphone(Product):
    efficiency: str
    model: str
    memory: int
    color: str

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        # Инициализируем свои атрибуты
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

        # Вызов родительского конструктора
        super().__init__(name, description, price, quantity)


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        # Инициализируем свои атрибуты
        self.country = country
        self.germination_period = germination_period
        self.color = color

        # Вызов родительского конструктора
        super().__init__(name, description, price, quantity)


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S21", "Cмартфон на android", "32000", "100")
    product2 = Product("Iphone 11", "Смартфон на IOS", "44000", "67")

    print(product1.name)
    print(product1.price)

    print(product1.name)
    print(product1.price)

    print(product2.name)
    print(product2.price)

    smartphone = Smartphone(
        "iPhone 17", "Флагман", "147000", "7", "Apple A19 Pro", "17 Pro", "1TB", "Black"
    )
    grass = LawnGrass("Трава", "Газонная", "1000", "50", "Япония", "28 дней", "Зеленая")
