def sorted_numbers(num):
    new_list = []
    for element in num:
        element = int(element)
        new_list.append(element)
    return sorted(new_list)


numbers = input().split()
print(sorted_numbers(numbers))