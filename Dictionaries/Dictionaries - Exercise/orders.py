products = {}
while True:
    info = input().split()
    product= info[0]
    if product == 'buy':
        break
    price = float(info[1])
    quantity = int(info[2])
    if product not in products:
        products[product] = 0
        products[product] = [price, quantity]
    elif product in products and price != products[product][0]:
        products[product][0] = price
        products[product][1] += quantity
    elif product in products and price == products[product][0]:
        products[product][1] += quantity
for key, value in products.items():
    print(f"{key} -> {products[key][0] * products[key][1]:.2f}")

