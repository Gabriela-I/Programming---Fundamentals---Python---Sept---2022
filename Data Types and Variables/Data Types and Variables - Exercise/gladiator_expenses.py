number_of_lost_fights = int(input())
helmet_price = float(input())
helmet_broken_count = 0
sword_price = float(input())
sword_broken_count = 0
shield_price = float(input())
shield_broken_count = 0
armor_price = float(input())
armor_broken_count = 0
for game in range(1, number_of_lost_fights + 1):
    if game % 2 == 0:
        helmet_broken_count += 1
    if game % 3 == 0:
        sword_broken_count += 1
    if game % 6 == 0:
        shield_broken_count += 1
    if game % 12 == 0:
        armor_broken_count += 1
expenses = helmet_price * helmet_broken_count + \
           sword_price * sword_broken_count + \
           shield_price * shield_broken_count + \
           armor_price * armor_broken_count
print(f"Gladiator expenses: {expenses:.2f} aureus")
