tail, body, head = input(), input(), input()

animal_list = [tail, body, head]
animal_list[0], animal_list[2] = animal_list[2], animal_list[0]

print(animal_list)