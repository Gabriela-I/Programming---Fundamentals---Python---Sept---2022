def add_stop(destinations, index, str):
    if 0 <= index < len(destinations):
        destinations = destinations[:index] + str + destinations[index:]
        print(destinations)
    else:
        print(destinations)
    return destinations


def remove_spot(destinations, start, end):
    if 0 <= start <= end < len(destinations):
        waste_str = destinations[start:end + 1]
        destinations = destinations.replace(waste_str, '')
        print(destinations)
    else:
        print(destinations)
    return destinations


def switch(destinations, old, new):
    if old in destinations:
        destinations = destinations.replace(old, new)
        print(destinations)
    else:
        print(destinations)
    return destinations


def print_result(destinations):
    print(f"Ready for world tour! Planned stops: {destinations}")


def main_function(destinations):
    while True:
        info = input().split(':')
        command = info[0]
        if command == 'Travel':
            break
        elif command == 'Add Stop':
            index, str = int(info[1]), info[2]
            destinations = add_stop(destinations, index, str)
        elif command == 'Remove Stop':
            start_index, end_index = int(info[1]), int(info[2])
            destinations = remove_spot(destinations, start_index, end_index)
        else:
            old_string, new_string = info[1], info[2]
            destinations = switch(destinations, old_string, new_string)
    print_result(destinations)


stops = input()
main_function(stops)
