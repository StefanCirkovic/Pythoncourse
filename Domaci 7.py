
products = {
    "hleb": {
        "cena": 100,
        "kolicina": 220
    },
    "pivo": {
        "cena": 150,
        "kolicina": 220
}
}

option = None
while option not in ["dodaj", "obrisi"]:
    option = input("Sta zelite odraditi, dodaj ili obrisi?").lower()


if option == "obrisi":
    product = None
    while product not in products:
         product = input("Koji proizvod zelite da obrisete? ").lower()

    del products[product]
    print(products)

elif option == "dodaj":
    product = None
    while product in products or product == None:
        product = input("Koji proizvod zelite da unesete?").lower()


    productPrice = None
    while productPrice == None or productPrice <= 0:
         productPrice =int(input("Unesite cenu proizvoda: "))

print(product, productPrice)

productAmount = None
while productAmount == None or productAmount <= 0:
    productAmount = int(input("Unesite kolicinu: "))

products[product] = {
    "cena": productPrice,
    "kolicina": productAmount
}

print(products)