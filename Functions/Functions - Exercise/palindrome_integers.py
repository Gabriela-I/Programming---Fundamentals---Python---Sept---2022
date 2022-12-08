def palindrome_numbers(num):
    for element in num:
        original_element = element
        reversed_num = 0
        while element != 0:
            digit = element % 10
            reversed_num = reversed_num * 10 + digit
            element //= 10
        if original_element == reversed_num:
            print(True)
            continue
        print(False)


numbers = list(map(int, input().split(', ')))
palindrome_numbers(numbers)


#Tamer

# def is_palindrome(number):
#     for num in number:
#         if num == num[::-1]:
#             print("True")
#         elif num != num[::-1]:
#             print("False")
#
#
# numbers = input().split(", ")
# is_palindrome(numbers)