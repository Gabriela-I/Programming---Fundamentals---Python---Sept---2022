def total_price(order, quantity):
    if order == 'coffee':
        return f'{quantity * 1.50:.2f}'
    elif order == 'water':
        return f'{quantity * 1.00:.2f}'
    if order == 'coke':
        return f'{quantity * 1.40:.2f}'
    if order == 'snacks':
        return f'{quantity * 2.00:.2f}'


product = input()
quantity_of_product = int(input())
print(total_price(product,quantity_of_product))