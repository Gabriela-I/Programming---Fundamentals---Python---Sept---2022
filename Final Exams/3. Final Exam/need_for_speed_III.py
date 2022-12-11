def drive(group, name, distance, power):
    if group[name][1] >= power:
        group[name][1] -= power
        group[name][0] += distance
        print(f"{name} driven for {distance} kilometers. {power} liters of fuel consumed.")
        if group[name][0] >= 100000:
            del group[name]
            print(f'Time to sell the {name}!')
    else:
        print("Not enough fuel to make that ride")


def refuel(group, name, power):
    group[name][1] += power
    if group[name][1] > 75:
        extra_fuel = power - (group[name][1] - 75)
        group[name][1] = 75
        print(f"{brand} refueled with {extra_fuel} liters")
    else:
        print(f"{brand} refueled with {power} liters")


def revert(group, name, distance):
    group[name][0] -= distance
    print(f"{name} mileage decreased by {distance} kilometers")
    if group[name][0] < 10000:
        group[name][0] = 10000


def print_cars(group):
    for key, value in group.items():
        print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")


numbers_of_cars = int(input())
cars = {}
for num in range(numbers_of_cars):
    auto, miles, fuel = input().split('|')
    cars[auto] = [int(miles), int(fuel)]
while True:
    command = input().split(' : ')
    if command[0] == 'Stop':
        print_cars(cars)
        break
    current_command, brand = command[0], command[1]
    if current_command == 'Drive':
        miles, fuel = int(command[2]), int(command[3])
        drive(cars,brand, miles, fuel)
    elif current_command == 'Refuel':
        fuel = int(command[2])
        refuel(cars, brand, fuel)
    elif current_command == 'Revert':
        miles = int(command[2])
        revert(cars, brand, miles)
