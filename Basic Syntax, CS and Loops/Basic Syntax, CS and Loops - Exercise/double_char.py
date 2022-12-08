string = input()
while string != 'End':
    if string == 'SoftUni':
        string = input()
        continue
    else:
        for index in range (len(string)):
            current_index = string[index]
            #double_index = current_index + current_index
            print(current_index * 2, end='')
        print()
    string = input()