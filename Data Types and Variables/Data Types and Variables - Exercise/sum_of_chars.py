number_of_chars = int(input())
total_sum = 0
for number in range(number_of_chars):
    current_chart = input()
    total_sum += ord(current_chart)
print(f"The sum equals: {total_sum}")
