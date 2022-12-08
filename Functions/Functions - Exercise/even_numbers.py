# def even_numbers(num):
#     for element in num:
#         element = int(element)
#         if element % 2 == 0:
#             return True
#         return False
#
#
# numbers = list(input().split())
# even_numbers_iterator = filter(even_numbers, numbers)
# print(list(map(int, even_numbers_iterator)))

numbers = map(int, input().split())
result = filter(lambda num: num % 2 == 0, numbers)
print(list(result))




