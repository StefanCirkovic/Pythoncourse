from Domaci21.product import Product
from Domaci21.shopping_cart import Shopping_cart

class Product:
    number_of_products = 0
    allowed_types = ["ios", "android"]
    number_of_types = {
        "android": 0,
        "ios": 0
    }

    def __init__(self, name, price, amount, type):

        if amount < 1:
            raise ValueError("Amount must be more than 0")

        if type not in Product.allowed_types:
            raise ValueError("Type is neither ios or android")


        self.name = name
        self.price = price
        self.amount = amount
        self.type = type
        Product.number_of_products += 1

        Product.number_of_types[type] += amount


class Shopping_cart:


    def __init__(self):
        self.items = []

    def add_product(self, item):
        self.items.append(item)

    def show_products(self):
        for item in self.items:
            print(item.name)




iPhone = Product("iPhone 16", 3500, 100, "ios")
Samsung = Product("Samsung A55", 1000, 25, "android")


phone_cart = Shopping_cart()
phone_cart.add_product(iPhone)
phone_cart.add_product(Samsung)



print(Product.number_of_types)