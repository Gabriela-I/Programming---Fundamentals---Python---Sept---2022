version = [int(number) for number in input().split('.')]
first = version[0]
second = version[1]
third = version[2]
for first_number in range(first, 9+1):
    for second_number in range(second, 9+1):
        for third_number in range(third, 9+1):
            third += 1
            if third == 10:
                third = 0
                second += 1
                if second == 10:
                    second = 0
                    first += 1
            print(f'{first}.{second}.{third}')
            break
        break
    break

