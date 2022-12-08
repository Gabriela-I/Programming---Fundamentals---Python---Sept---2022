def sum_of_odd_and_even(number):
    odd_sum = 0
    even_sum = 0
    for digit in number:
        digit = int(digit)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number_as_string = input()
#odd_sum, even_sum = sum_of_odd_and_even(number_as_string)
print(sum_of_odd_and_even(number_as_string))