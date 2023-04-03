import re

locations = input()
regex = r"(?<=([=\/]))[A-Z][A-Za-z][A-Za-z]+(?=\1)"

travel_points = 0
destinations = []

matches = list(re.finditer(regex, locations))

for match in matches:
    travel_points += len(match.group())
    destinations.append(match.group())


print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
