items = input().split(', ')
result = {item:ord(item) for item in items}
print(result)