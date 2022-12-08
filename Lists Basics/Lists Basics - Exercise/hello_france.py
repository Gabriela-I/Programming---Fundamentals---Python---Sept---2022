collection_of_items = input().split('|')
budget = float(input())
new_prices = []
first_budget = budget
for item in collection_of_items:
    item_list = item.split('->')
    items = item_list[0]
    price = float(item_list[1])
    if budget >= price:
        if items == 'Clothes' and price <= 50 or \
                items == 'Shoes' and price <= 35.00 or \
                items == 'Accessories' and price <= 20.50:
            budget -= price
            new_prices.append(price * 1.4)
for element in new_prices:
    print(f'{element:.2f}', end=' ')
print()
profit = sum(new_prices) - first_budget + budget
print(f"Profit: {profit:.2f}")
if sum(new_prices) + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
