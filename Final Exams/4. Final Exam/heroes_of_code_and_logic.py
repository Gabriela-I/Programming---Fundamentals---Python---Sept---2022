def cast_spell(group, hero, mp_needed, spell_name):
    if group[hero][1] >= mp_needed:
        group[hero][1] -= mp_needed
        print(f"{hero} has successfully cast {spell_name} and now has {group[hero][1]} MP!")
    elif group[hero][1] < mp_needed:
        print(f"{hero} does not have enough MP to cast {spell_name}!")


def take_damage(group, hero, destruction, striker):
    group[hero][0] -= destruction
    if group[hero][0] > 0:
        print(f"{hero} was hit for {destruction} HP by {striker} and now has {group[hero][0]} HP left!")
    else:
        del group[hero]
        print(f"{hero} has been killed by {striker}!")


def recharge(group, hero, quantity):
    group[hero][1] += quantity
    max_mp = 200
    if group[hero][1] > 200:
        waste_bonus = group[hero][1] - max_mp
        bonus = quantity - waste_bonus
        group[hero][1] = 200
        print(f"{hero} recharged for {bonus} MP!" )
    else:
        bonus = quantity
        print(f"{hero} recharged for {bonus} MP!")


def heal(group, hero, quantity):
    group[hero][0] += quantity
    max_hp = 100
    if group[hero][0] > 100:
        waste_bonus = group[hero][0] - max_hp
        bonus = quantity - waste_bonus
        group[hero][0] = 100
        print(f"{hero} healed for {bonus} HP!")
    else:
        bonus = quantity
        print(f"{hero} healed for {bonus} HP!")


number_of_heroes = int(input())
heroes = {}
for num in range(number_of_heroes):
    name, hp, mp = input().split()
    heroes[name] = [int(hp), int(mp)]
command = input()
while command != 'End':
    info = command.split(' - ')
    action = info[0]
    if action == 'CastSpell':
        soldier, needed_mp, spell = info[1], int(info[2]), info[3]
        cast_spell(heroes, soldier, needed_mp, spell)
    elif action == 'TakeDamage':
        soldier, damage, attacker = info[1], int(info[2]), info[3]
        take_damage(heroes, soldier, damage, attacker)
    elif action == 'Recharge':
        soldier, amount = info[1], int(info[2])
        recharge(heroes, soldier, amount)
    elif action == 'Heal':
        soldier, amount = info[1], int(info[2])
        heal(heroes, soldier, amount)

    command = input()

for hero, info in heroes.items():
    print(f'{hero}\n   HP: {info[0]}\n  MP: {info[1]}')