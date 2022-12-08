def smallest_of_three_numbers (numbers):
    return min(numbers)


first_number = int(input())
second_number = int(input())
third_number = int(input())
list_with_numbers = [first_number, second_number, third_number]
print(smallest_of_three_numbers(list_with_numbers))