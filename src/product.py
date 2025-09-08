class Product:
    name: str
    description: str
    price: float
    quantity: int
    product_count = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S21", "Cмартфон на android", "32000", "100")
    product2 = Product("Iphone 11", "Смартфон на IOS", "44000", "67")

    print(product1.name)
    print(product1.price)

    print(product2.name)
    print(product2.price)
