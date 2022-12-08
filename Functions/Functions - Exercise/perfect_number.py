def perfect_number(num):
    list_with_divisors = []
    for element in range(1, num):
        if num % element == 0:
            list_with_divisors.append(element)
    if sum(list_with_divisors) == num:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(perfect_number(number))
