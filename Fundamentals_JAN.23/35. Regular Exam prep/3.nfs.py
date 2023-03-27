n = int(input())    # no. of cars
car_mileage = {}
car_fuel = {}

for _ in range(n):
    line = input().split("|")
    car = line[0]
    mileage = int(line[1])
    fuel = int(line[2])

    car_mileage[car] = mileage
    car_fuel[car] = fuel

while True:
    line = input()

    if line == "Stop":
        break

    line_args = line.split(" : ")
    command = line_args[0]
# "Drive : {car} : {distance} : {fuel}
    if command == "Drive":
        car = line_args[1]
        distance = int(line_args[2])
        fuel = int(line_args[3])

        if car_fuel[car] < fuel:
            print("Not enough fuel to make that ride")
        else:
            car_mileage[car] += distance
            car_fuel[car] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if car_mileage[car] >= 100000:
                del car_mileage[car]
                print(f"Time to sell the {car}!")

    elif command == "Refuel":
        car = line_args[1]
        fuel = int(line_args[2])

        if car_fuel[car] + fuel > 75:
            print(f"{car} refueled with {75 - car_fuel[car]} liters")
            car_fuel[car] = 75

        else:
            print(f"{car} refueled with {fuel} liters")
            car_fuel[car] += fuel

    elif command == "Revert":
        car = line_args[1]
        kilometers = int(line_args[2])

        if car_mileage[car] - kilometers < 10000:
            car_mileage[car] = 10000
        else:
            car_mileage[car] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

for car in car_mileage:
    print(f"{car} -> Mileage: {car_mileage[car]} kms, Fuel in the tank: {car_fuel[car]} lt.")
