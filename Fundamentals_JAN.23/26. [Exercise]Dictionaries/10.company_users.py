database = {}

while True:
    line = input()

    if line == "End":
        break

    company, id = line.split(" -> ")

    if company not in database:
        database[company] = [id]
    
    else:
        database[company].append(id)
    
    if database[company].count(id) > 1:
        database[company].reverse()
        database[company].remove(id)
        database[company].reverse()

for company, empoyees in database.items():
    print(company)
    print(f"-- "+"\n-- ".join(empoyees))
