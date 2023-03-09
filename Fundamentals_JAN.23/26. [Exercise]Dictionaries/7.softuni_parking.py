parking_lot = {}

n = int(input())

for _ in range(n):
    args = input().split()
    command = args[0]
    username = args[1]

    if command == "register":
        license_plate = args[2]
        if username in parking_lot:
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            parking_lot[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    
    else:
        if username not in parking_lot:
            print(f"ERROR: user {username} not found")
        
        else:
            parking_lot.pop(username)
            print(f"{username} unregistered successfully")

for user, plate in parking_lot.items():
    print(f"{user} => {plate}")

