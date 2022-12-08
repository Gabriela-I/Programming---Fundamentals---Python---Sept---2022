goal_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
line = input().split()
junk = {}
obtained = False
while not obtained:
    for item in range(0, len(line), 2):
        quantity = line[item]
        material = line[item + 1].lower()
        if material in goal_materials:
            goal_materials[material] += int(quantity)
            if goal_materials[material] >= 250:
                goal_materials[material] -= 250
                if material == 'shards':
                    print('Shadowmourne obtained!')
                elif material == 'motes':
                    print('Dragonwrath obtained!')
                elif material == 'fragments':
                    print('Valanyr obtained!')
                obtained = True
                break

        else:
            if material not in junk:
                junk[material] = 0
            junk[material] += int(quantity)
    if obtained is True:
        break
    line = input().split()
print(f"shards: {goal_materials['shards']}\nfragments: {goal_materials['fragments']}\nmotes: {goal_materials['motes']}")
for key,value in junk.items():
    print(f'{key}: {value}')