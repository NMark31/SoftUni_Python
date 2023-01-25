n = int(input())

list_of_positives = []
list_of_negatives = []
# positives_count = 0
# negatives_sum = 0

for _ in range(n):
    number = int(input())

    if number >= 0:
        list_of_positives.append(number)
        # positives_count += 1
    
    else:
        list_of_negatives.append(number)
        # negatives_sum += number

print(list_of_positives)
print(list_of_negatives)
print(f"Count of positives: {len(list_of_positives)}\nSum of negatives: {sum(list_of_negatives)}")
