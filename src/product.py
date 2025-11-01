class Product:
    name: str
    description: str
    price: float
    quantity: int
    product_count = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            return
        return (self.price * self.quantity) + (other.price * other.quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
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


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S21", "Cмартфон на android", "32000", "100")
    product2 = Product("Iphone 11", "Смартфон на IOS", "44000", "67")

    print(product1.name)
    print(product1.price)

    print(product1.name)
    print(product1.price)

    print(product2.name)
    print(product2.price)
