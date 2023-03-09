key_resources = {}
junk_resources = {}
legendary_obtained = False

while not legendary_obtained:
    line = input().split()
    
    for idx in range(0, len(line), 2):
        quantity = int(line[idx])
        resource = line[idx+1].lower()

        if resource == "shards":
            if resource not in key_resources:
                key_resources[resource] = quantity
            else:
                key_resources[resource] += quantity
                if key_resources[resource] >= 250:
                    print(f"Shadowmourne obtained!")
                    key_resources[resource] -= 250
                    legendary_obtained = True
                    break

        elif resource == "fragments":
            if resource not in key_resources:
                key_resources[resource] = quantity
            else:
                key_resources[resource] += quantity
            if key_resources[resource] >= 250:
                print(f"Valanyr obtained!")
                key_resources[resource] -= 250
                legendary_obtained = True
                break

        elif resource == "motes":
            if resource not in key_resources:
                key_resources[resource] = quantity
            else:
                key_resources[resource] += quantity
            if key_resources[resource] >= 250:
                print(f"Dragonwrath obtained!")
                key_resources[resource] -= 250
                legendary_obtained = True
                break
        
        else:
            if resource not in junk_resources:
                junk_resources[resource] = quantity
            else:
                junk_resources[resource] += quantity


print(f"shards: {key_resources.get('shards', 0)}")
print(f"fragments: {key_resources.get('fragments', 0)}")
print(f"motes: {key_resources.get('motes', 0)}")

for resource, quantity in junk_resources.items():
    print(f"{resource}: {quantity}")


        