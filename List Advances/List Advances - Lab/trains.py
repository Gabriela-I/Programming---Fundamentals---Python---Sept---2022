number_of_wagons = int(input())
wagons = [0 for wagon in range(number_of_wagons)]
while True:
    command = input()
    if command == 'End':
        break
    current_command = command.split()[0]
    if current_command == 'add':
        number_of_people = int(command.split()[1])
        wagons[-1] += number_of_people
    elif current_command == 'insert':
        number_of_people = int(command.split()[2])
        index = int(command.split()[1])
        wagons[index] += number_of_people
    else:
        number_of_people = int(command.split()[2])
        index = int(command.split()[1])
        wagons[index] -= number_of_people
print(wagons)