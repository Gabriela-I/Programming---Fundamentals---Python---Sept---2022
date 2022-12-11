import re

total_calories = 0
text = input()
pattern = r"(\||#)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)+\1"
match = re.findall(pattern, text)
result = ''
for info in match:
    total_calories += int(info[3])
    result += f"Item: {info[1]}, Best before: {info[2]}, Nutrition: {info[3]}\n"
last_days = total_calories // 2000
print(f"You have food to last you for: {last_days} days!")
print(result)