path = input()
result = ''
strength = 0
for index in range(len(path)):
    if strength > 0 and path[index] != '>':
        strength -= 1
    elif path[index] == '>':
        strength += int(path[index + 1])
        result += path[index]
    else:
        result += path[index]
print(result)


