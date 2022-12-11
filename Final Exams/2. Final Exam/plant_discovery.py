number_of_plants = int(input())
plants = {}
for num in range(number_of_plants):
    plant, rarity = input().split('<->')
    if plant not in plants:
        plants[plant] = {'rarity': rarity, 'rating': []}
    else:
        plants[plant]['rarity'] += rarity

while True:
    line = input()
    if line == 'Exhibition':
        break
    info = line.split(' ')
    command, name_of_plant = info[0], info[1]
    if command == 'Rate:':
        some_value = int(info[3])

        if name_of_plant in plants:
            plants[name_of_plant]['rating'].append(some_value)
        else:
            print('error')

    elif command == 'Update:':
        some_value = int(info[3])
        if name_of_plant in plants:
            plants[name_of_plant]['rarity'] = some_value
        else:
            print('error')

    else:
        if name_of_plant in plants:
            plants[name_of_plant]['rating'] = []
        else:
            print('error')

print("Plants for the exhibition:")
for plant_name, value in plants.items():
    average = 0
    if len(plants[plant_name]['rating']) != 0:
        average = sum(plants[plant_name]['rating'])/len(plants[plant_name]['rating'])
    print(f'- {plant_name}; Rarity: {value["rarity"]}; Rating: {average:.2f}')


