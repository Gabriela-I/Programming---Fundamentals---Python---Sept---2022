def calculate(number_one, number_two, operator):
    if operator == 'multiply':
        return number_one * number_two
    elif operator == 'divide':
        return int(number_one / number_two)
    elif operator == 'add':
        return number_one + number_two
    elif operator == 'subtract':
        return number_one - number_two


operator_input = input()
first_number = int(input())
second_number = int(input())
print(calculate(first_number, second_number, operator_input))