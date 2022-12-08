number_of_people = int(input())
days = int(input())
coins_counter = 0
for day in range(1, days + 1):

    if day % 10 == 0:
        number_of_people -= 2
    if day % 15 == 0:
        number_of_people += 5
    if day % 3 == 0:
        coins_counter -= 3 * number_of_people
    if day % 5 == 0:
        coins_counter += 20 * number_of_people
        if day % 3 == 0:
            coins_counter -= 2 * number_of_people
    coins_counter += 50
    coins_counter -= 2 * number_of_people
coins_per_person = coins_counter / number_of_people
print(f"{number_of_people} companions received {int(coins_per_person)} coins each.")