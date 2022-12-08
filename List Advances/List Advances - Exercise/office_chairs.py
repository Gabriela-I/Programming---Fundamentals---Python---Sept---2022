number_of_rooms = int(input())
enough_chairs = True
free_chairs = 0
needed_chairs = 0
for room in range(1, number_of_rooms + 1):
    information = input().split()
    chairs_number = information[0]
    visitors_number = int(information[1])
    if len(chairs_number) > visitors_number:
        free_chairs += len(chairs_number) - visitors_number
    elif len(chairs_number) < visitors_number:
        enough_chairs = False
        needed_chairs = visitors_number - len(chairs_number)
        print(f"{needed_chairs} more chairs needed in room {room}")
if enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")
