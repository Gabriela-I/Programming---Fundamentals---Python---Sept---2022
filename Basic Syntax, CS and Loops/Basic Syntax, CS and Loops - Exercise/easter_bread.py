budget = float(input())
flour_price = float(input())
count_bread = 0
count_eggs = 0
eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25 / 4
bread_price = flour_price + milk_price + eggs_price
while budget >= bread_price:
    budget -= bread_price
    count_eggs += 3
    count_bread += 1
    if count_bread % 3 == 0:
        count_eggs -= count_bread - 2
print(f"You made {count_bread} loaves of Easter bread! Now you have {count_eggs} eggs and {budget:.2f}BGN left.")