string_of_numbers = input().split()
opposite_numbers = []
for element in string_of_numbers:
    current_element = -int(element)
    opposite_numbers.append(current_element)
print(opposite_numbers)