num_of_pairs = int(input())
synonyms = {}

for _ in range(num_of_pairs):
    key = input()
    value = input()

    if key not in synonyms:
        synonyms[key] = []
    
    synonyms[key].append(value)

for key, value in synonyms.items():
    print(f"{key} - {', '.join(value)}")
