import re

location = input()
pattern = r"([=|\/])([A-Z][A-Za-z]{2,})\1"
match = re.findall(pattern,location)
destinations = []
travel_points = 0
for locations in match:
    travel_points += len(locations[1])
    destinations.append(locations[1])
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")