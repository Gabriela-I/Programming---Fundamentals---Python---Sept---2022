import re

line = input()
pattern = r"\b_([a-z0-9A-Z]+)\b"
result = re.findall(pattern, line)
print(','.join(result))