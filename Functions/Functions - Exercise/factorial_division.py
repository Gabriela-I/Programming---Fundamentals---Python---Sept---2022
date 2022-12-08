def factorial_division(one, two):
    factorial_one = 1
    factorial_two = 1
    for element in range(1, one + 1):
        factorial_one *= element
    for element in range(1, two + 1):
        factorial_two *= element
    return f'{factorial_one / factorial_two:.2f}'


first_number = int(input())
second_number = int(input())
print(factorial_division(first_number, second_number))
