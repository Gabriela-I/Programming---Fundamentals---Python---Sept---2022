command = ''
count_coffee = 0
while command != 'END':
    if command.lower() == 'coding' \
            or command.lower() == 'dog' \
            or command.lower() == 'cat' \
            or command.lower() == 'movie':
        if command.islower():
            count_coffee += 1
        else:
            count_coffee += 2
    command = input()
if count_coffee > 5:
    print("You need extra sleep")
else:
    print(count_coffee)