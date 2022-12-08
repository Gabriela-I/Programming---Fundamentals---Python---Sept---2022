country_names = input().split(', ')
capital_cities = input().split(', ')
result = {country_names[index]:capital_cities[index] for index in range(len(country_names))}
for key, value in result.items():
    print(f"{key} -> {value}")