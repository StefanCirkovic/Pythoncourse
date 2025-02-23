

class Product:

    number_of_products = 0

    def __init__(self, name, price, amount, type):
        self.name = name
        self.price = price
        self.amount = amount
        self.type = type
        Product.number_of_products += 1

