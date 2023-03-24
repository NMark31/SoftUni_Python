import re

dates = input()
regex = "\\b(?P<Day>\\d{2})(?P<Sep>[-.\\/])(?P<Month>[A-Z][a-z]{2})\\2(?P<Year>\\d{4})\\b"

matches = re.finditer(regex, dates)

for match in matches:
    match_data = match.groupdict()
    print(f"Day: {match_data['Day']}, Month: {match_data['Month']}, Year: {match_data['Year']}")