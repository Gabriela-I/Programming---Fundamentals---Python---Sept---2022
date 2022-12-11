def plunder(cities, this_city, all_people, this_gold):
    cities[this_city][0] -= all_people
    cities[this_city][1] -= this_gold
    print(f"{this_city} plundered! {this_gold} gold stolen, {all_people} citizens killed.")
    if cities[this_city][0] <= 0 or cities[this_city][1] <= 0:
        del cities[this_city]
        print(f'{this_city} has been wiped off the map!')


def prosper(cities, this_city, this_gold):
    if this_gold < 0:
        print("Gold added cannot be a negative number!")
    else:
        cities[this_city][1] += this_gold
        print(f"{this_gold} gold added to the city treasury. {this_city} now has {cities[this_city][1]} gold.")


def print_towns(cities):
    if len(cities) == 0:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")
    else:
        print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
        for key, value in cities.items():
            print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')

info = input()
towns = {}
while info != 'Sail':
    if info == 'Sail':
        break
    city, population, gold = info.split('||')
    if city not in towns:
        towns[city] = [int(population), int(gold)]
    else:
        towns[city][0] += int(population)
        towns[city][1] += int(gold)
    info = input()

while True:
    event = input().split('=>')
    if event[0] == 'End':
        print_towns(towns)
        break
    elif event[0] == 'Plunder':
        town, people, gold = event[1], int(event[2]), int(event[3])
        plunder(towns, town, people, gold)
    else:
        town, gold = event[1], int(event[2])
        prosper(towns, town, gold)

