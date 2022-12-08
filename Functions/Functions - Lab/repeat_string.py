# def repeat_string(word, counter):
#     return word * counter
#
#
# string_input = input()
# count_of_repeat = int(input())
# print(repeat_string(string_input, count_of_repeat))


repeat_string = lambda word, counter: word * counter


string_input = input()
count_of_repeat = int(input())
print(repeat_string(string_input, count_of_repeat))