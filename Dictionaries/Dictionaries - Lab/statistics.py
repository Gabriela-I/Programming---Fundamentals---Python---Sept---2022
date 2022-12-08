items = input()
statistics = {}
while items != 'statistics':
    product = items.split(':')[0]
    quantity = int(items.split(':')[1])
    if product not in statistics.keys():
        statistics[product] = 0
    statistics[product] += quantity
    items = input()
print('Products in stock:')
for (product,quantity) in statistics.items():
    print(f'- {product}: {quantity}')
print(f'Total Products: {len(statistics)}')
print(f'Total Quantity: {sum(statistics.values())}')