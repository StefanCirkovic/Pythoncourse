
# Nestovani dictionary
shops = {
    "Maxi": {
        "Hleb": 100,
        "Novine": 50
    },
     "Idea": {
         "Hleb": 95,
         "Novine": 62
    },
     "Roda": {
         "Hleb": 97,
         "Novine": 60
     },
     "Free shop": {
         "Novine": 62
     },
     "Pijaca": {
         "Hleb": 99
     }
}

total_bread_price = 0
total_bread_shops = 0
highest_bread_price = 0
highest_bread_price_shop = ""


for shop_name, items in shops.items():
    if "Hleb" in items:
        total_bread_price += items["Hleb"]
        total_bread_shops += 1
        if highest_bread_price < items["Hleb"]:
            highest_bread_price = items["Hleb"]
            highest_bread_price_shop = shop_name
    else:
        continue

total_shops = len(shops)

average_bread_price = total_bread_price / total_bread_shops

print(average_bread_price)
print(highest_bread_price_shop)