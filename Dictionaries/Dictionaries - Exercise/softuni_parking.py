number_of_commands = int(input())
data = {}
for command in range(number_of_commands):
    line = input().split()
    current_command = line[0]
    if current_command == 'register':
        name = line[1]
        number = line[2]
        if name in data:
            print(f'ERROR: already registered with plate number {number}')
        else:
            data[name] = number
            print(f"{name} registered {number} successfully")
    else:
        name = line[1]
        if name not in data:
            print(f"ERROR: user {name} not found")
        else:
            del data[name]
            print(f"{name} unregistered successfully")
for key,value in data.items():
    print(f"{key} => {value}")