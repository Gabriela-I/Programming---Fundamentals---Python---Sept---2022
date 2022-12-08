first_line = input().split(', ')
second_line = input().split(', ')
new_list = []
for word in first_line:
    for item in second_line:
        if word in item:
            if word not in new_list:
                new_list.append(word)
result = new_list
print(result)