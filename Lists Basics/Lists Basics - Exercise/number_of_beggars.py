money = input().split(', ')
count_of_beggars = int(input())
starting_index = 0
final_sum = []
money_as_digits = []
for element in money:
    money_as_digits.append(int(element))
while starting_index < count_of_beggars:
    sum_of_element = 0
    for part in range(starting_index,len(money_as_digits), count_of_beggars):
        sum_of_element += money_as_digits[part]
    final_sum.append(sum_of_element)
    starting_index += 1
print(final_sum)
