food_and_quantities = input().split()
bakery = {}
for item in range(0,len(food_and_quantities), 2):
    key = food_and_quantities[item]
    value = food_and_quantities[item + 1]
    bakery[key] = int(value)
print(bakery)
