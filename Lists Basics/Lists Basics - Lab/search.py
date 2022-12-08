number_of_words = int(input())
word = input()
list_with_strings = []
second_list_with_strings = []
for element in range(number_of_words):
    current_string = input()
    list_with_strings.append(current_string)
    if word in current_string:
            second_list_with_strings.append(current_string)
print(list_with_strings)
print(second_list_with_strings)


# my code
# number_of_words = int(input())
# word = input()
# list_with_strings = []
# second_list_with_strings = []
# for element in range(number_of_words):
#     current_string = input()
#     list_with_strings.append(current_string)
#     second_list_with_strings.append(current_string)
#     for strings in list_with_strings:
#         strings.split()
#         if word not in strings:
#             list_with_strings.remove(strings)
# print(second_list_with_strings)
# print(list_with_strings)
