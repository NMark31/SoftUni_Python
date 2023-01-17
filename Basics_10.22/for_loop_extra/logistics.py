num_of_loads = int(input())
bus_loads = 0 
truck_loads = 0 
train_loads = 0
bus_price = 0
truck_price = 0
train_price = 0
average_price = 0

for i in range(num_of_loads):
    weight = int(input())

    if weight <= 3:
        bus_loads += weight
        bus_price += weight * 200

    elif weight < 12:
        truck_loads += weight
        truck_price += weight * 175
    else:
        train_loads += weight
        train_price += weight * 120

total_weight = bus_loads + truck_loads + train_loads
average_price = (bus_price + truck_price + train_price) / total_weight


print(f'{average_price:.2f}')
print(f'{(bus_loads / total_weight) * 100:.2f}%')
print(f'{(truck_loads / total_weight) * 100:.2f}%')
print(f'{(train_loads / total_weight) * 100:.2f}%')
