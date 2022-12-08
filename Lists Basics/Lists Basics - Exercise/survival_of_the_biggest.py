import sys

numbers = input().split()
numbers_to_remove_count = int(input())
numbers_as_digit = []
for elements in numbers:
    numbers_as_digit.append(int(elements))
numbers_to_remove = []
while len(numbers_to_remove) < numbers_to_remove_count:
    current_number = sys.maxsize
    for number in range(len(numbers_as_digit)):
        if numbers_as_digit[number] < current_number:
            current_number = numbers_as_digit[number]
    numbers_to_remove.append(current_number)
    numbers_as_digit.remove(current_number)
print(*numbers_as_digit, sep=', ')
