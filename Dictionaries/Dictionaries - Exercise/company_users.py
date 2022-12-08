all_companies = {}
while True:
    info = input()
    if info == 'End':
        break
    company, ids = info.split(' -> ')
    if company not in all_companies:
        all_companies[company] = []
        all_companies[company].append(ids)
    elif company in all_companies and ids not in all_companies[company]:
        all_companies[company].append(ids)
for key, value in all_companies.items():
    print(key)
    for ids in value:
        print(f'-- {ids}')

