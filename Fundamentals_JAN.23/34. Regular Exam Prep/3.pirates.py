cities_population = {}
cities_gold = {}

while True:
    line = input()

    if line == "Sail":
        break

    city, population, gold = line.split("||")

    if city in cities_population:
        cities_population[city] += int(population)
        cities_gold[city] += int(gold)

    else:
        cities_population[city] = int(population)
        cities_gold[city] = int(gold)

while True:
    event = input()

    if event == "End":
        break

    args = event.split("=>")
    action = args[0]
    town = args[1]

    if action == "Plunder":
        people = int(args[2])
        gold = int(args[3])

        cities_population[town] -= people
        cities_gold[town] -= gold

        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities_gold[town] <= 0 or cities_population[town] <= 0:
            del cities_gold[town]
            del cities_population[town]
            print(f"{town} has been wiped off the map!")
    
    else:
        gold = int(args[2])

        if gold >= 0:
            cities_gold[town] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities_gold[town]} gold.")

        else:
            print("Gold added cannot be a negative number!")

if cities_population:
    print(f"Ahoy, Captain! There are {len(cities_population)} wealthy settlements to go to:")

    for city in cities_population:
        print(f"{city} -> Population: {cities_population[city]} citizens, Gold: {cities_gold[city]} kg")

else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")

