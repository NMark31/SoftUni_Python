n = int(input())

plants = {}
ratings = {}

for _ in range(n):
    plant, rarity = input().split("<->")

    plants[plant] = rarity
    ratings[plant] = []

while True:
    line = input()

    if line == "Exhibition":
        break

    commands = line.split(": ")
    command = commands[0]
    args = commands[1].split(" - ")

    if args[0] in plants:
        if command == "Rate":
            plant = args[0]
            rating = int(args[1])
            ratings[plant].append(rating) 
                
        elif command == "Update":
            plant = args[0]
            new_rarity = int(args[1])
            plants[plant] = new_rarity

        else:
            plant = args[0]
            ratings[plant].clear()
    else:
        print("error")
print("Plants for the exhibition:")

for plant, value in plants.items():
    if ratings[plant]:
        avg_rating = sum(ratings[plant]) / len(ratings[plant])
    else:
        avg_rating = 0

    print(f"- {plant}; Rarity: {value}; Rating: {avg_rating:.2f}")