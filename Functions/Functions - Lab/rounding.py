numbers = input().split()
rounded_numbers = []
list_with_numbers = []
for element in numbers:
    list_with_numbers.append(float(element))
for part in list_with_numbers:
    rounded_numbers.append(round(part))
print(rounded_numbers)