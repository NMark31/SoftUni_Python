phonebook = {}

line = input()

while "-" in line:
    name, phone_number = line.split("-")
    
    phonebook[name] = phone_number

    line = input()

n = int(line)

for _ in range(n):
    searched_name = input()

    if searched_name not in phonebook:
        print(f"Contact {searched_name} does not exist.")
    
    else:
        print(f"{searched_name} -> {phonebook[searched_name]}")
    

