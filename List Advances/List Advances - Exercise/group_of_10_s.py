numbers = list(map(int, input().split(', ')))
group = 10
max_num = 0
while len(numbers) > 0:
    list_of_numbers = []
    for num in numbers[:]:
        if num <= group:
            list_of_numbers.append(num)
            numbers.remove(num)
    print(f"Group of {group}'s: {list_of_numbers}")
    group += 10