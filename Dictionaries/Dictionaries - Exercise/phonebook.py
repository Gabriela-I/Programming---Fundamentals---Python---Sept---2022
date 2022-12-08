phonebook = {}
while True:
    entry = input()
    if '-' not in entry:
        number_of_names = int(entry)
        break
    name, number = entry.split('-')
    phonebook[name] = number
for num in range(number_of_names):
    current_name = input()
    if current_name in phonebook:
        print(f"{current_name} -> {phonebook[current_name]}")
    else:
        print(f"Contact {current_name} does not exist.")

