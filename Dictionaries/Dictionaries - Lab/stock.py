food_and_quantities = input().split()
stock = {}
searched_products = input().split()
for item in range(0,len(food_and_quantities), 2):
    key = food_and_quantities[item]
    value = food_and_quantities[item + 1]
    stock[key] = int(value)
for item in searched_products:
    if item in stock.keys():
        print(f"We have {stock[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
