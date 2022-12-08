# my

# def minimum_number(num):
#     min_num = min(num)
#     return min_num
#
#
# def maximum_number(num):
#     max_num = max(num)
#     return max_num
#
#
# def sum_of_all_numbers(num):
#     sum_numbers = sum(num)
#     return sum_numbers
#
#
# numbers = list(map(int, input().split(' ')))
# min_num = minimum_number(numbers)
# max_num = maximum_number(numbers)
# sum_numbers = sum_of_all_numbers(numbers)
# print(f"The minimum number is {min_num}")
# print(f"The maximum number is {max_num}")
# print(f"The sum number is: {sum_numbers}")


#MitkoVtori
# def min_number(numbers):
#     minimum_number = min(numbers)
#     return f'The minimum number is {minimum_number}'
#
#
# def max_number(numbers):
#     maximum_number = max(numbers)
#     return f'The maximum number is {maximum_number}'
#
#
# def sum_numbers(numbers):
#     sum_number = sum(numbers)
#     return f'The sum number is: {sum_number}'
#
#
# all_numbers = list(map(int, input().split(' ')))
# print(min_number(all_numbers))
# print(max_number(all_numbers))
# print(sum_numbers(all_numbers))

#Tamer
def min_max_and_sum(number):
    return min(number), max(number), sum(number)


numbers = list(map(int, input().split(' ')))
min_of_numbers, max_of_numbers, sum_of_numbers = min_max_and_sum(numbers)
print(f"The minimum number is {min_of_numbers}")
print(f"The maximum number is {max_of_numbers}")
print(f"The sum number is: {sum_of_numbers}")
