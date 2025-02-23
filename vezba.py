
from Product import Product
from ShoppingCart import ShoppingCart

iPhone16 = Product("Iphone 16 pro max", 1500, 500, "IOS")
samsungS23Pro = Product("Samsung S23 Pro", 1200, 200, "Android")
samsungA55 = Product("Samsung A55", 500, 5, "Android")

phoneCart = ShoppingCart()
phoneCart.add_product(samsungS23Pro)

phoneCart.showProducts()