class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        products_list = []
        for product in self.__products:
            product_conclusion = f"{product.name}, {int(product.price)} руб. Остаток: {product.quantity} шт."
            products_list.append(product_conclusion)

        return "\n".join(products_list)
