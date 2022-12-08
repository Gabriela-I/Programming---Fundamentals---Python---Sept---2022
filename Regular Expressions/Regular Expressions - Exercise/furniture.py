import re

furniture = []
total_money = []
info = input()
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
while info != 'Purchase':
    match = re.search(pattern, info)
    if match:
        furniture.append(match.group(1))
        total_money.append(float(match.group(2)) * int(match.group(3)))

    info = input()
print('Bought furniture:')
for item in furniture:
    print(item)
print(f"Total money spend: {sum(total_money):.2f}")