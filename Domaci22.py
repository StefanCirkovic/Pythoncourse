from product import Product
from Shopping_cart import Shopping_cart

iPhone = Product()
Samsung = Product()

iPhone.create("iPhone 16", 3500, 100, "ios")
iPhone.check_if_user_exists("iPhone 16fdvf")
iPhone.increment_number_of_products_for_type("ios", 10)

Samsung.create("Samsung A55", 1000, 25, "android")
Samsung.check_if_user_exists("Samsung A55fdvf")
Samsung.increment_number_of_products_for_type("android", 50)

phone_cart = Shopping_cart()
phone_cart.add_product(iPhone)
phone_cart.add_product(Samsung)



print(Product.number_of_types)