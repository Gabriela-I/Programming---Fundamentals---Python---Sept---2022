budget = int(input())
command = input()
total_prices = 0
while command != 'End':
    current_price = int(command)
    total_prices += current_price
    if total_prices > budget:
        print("You went in overdraft!")
        break

    command = input()
else:
    print("You bought everything needed.")