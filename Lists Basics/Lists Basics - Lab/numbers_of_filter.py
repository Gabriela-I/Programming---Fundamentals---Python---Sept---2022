number_of_lines = int(input())
command_even = 'even'
command_odd = 'odd'
command_positive = 'positive'
command_negative = 'negative'
my_list = []
for _ in range(number_of_lines):
    current_number = int(input())
    my_list.append(current_number)
command = input()
filter_list = []
for element in my_list:
    if element >= 0 and command == command_positive:
        filter_list.append(element)
    elif element < 0 and command == command_negative:
        filter_list.append(element)
    elif element % 2 == 0 and command == command_even:
        filter_list.append(element)
    elif element % 2 != 0 and command == command_odd:
        filter_list.append(element)
print(filter_list)
