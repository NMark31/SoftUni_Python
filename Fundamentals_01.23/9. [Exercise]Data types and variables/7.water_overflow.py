n = int(input())
capacity = 255
liters_count = 0

for _ in range(n):
    liters = int(input())

    if liters > capacity:
        print(f"Insufficient capacity!")
        continue
    
    capacity -= liters
    liters_count += liters

print(liters_count)
