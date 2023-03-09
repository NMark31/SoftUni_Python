countries = input().split(", ")
capitals = input().split(", ")

capitals_and_coutries = dict(zip(countries, capitals))

for country, capital in capitals_and_coutries.items():
    print(f"{country} -> {capital}")
