import re

line = input()
word = input()
pattern = fr'\b{word}\b'
result = re.findall(pattern, line, re.IGNORECASE)
print(len(result))