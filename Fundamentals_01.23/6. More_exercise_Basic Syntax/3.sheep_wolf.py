animals = input()
animals_to_list = []

animals_to_list = animals.split(", ")

for a in range(len(animals_to_list)):
    if a == len(animals_to_list) - 1:
        print("Please go away and stop eating my sheep")

    elif animals_to_list[a] == "wolf":
        print(f'Oi! Sheep number {len(animals_to_list) - 1 - a}! You are about to be eaten by a wolf!')
        break