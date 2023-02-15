n = int(input())

free_chairs = 0
chairs_sufficient = True

for room in range(1, n + 1):
    chairs, visitors = input().split()

    if len(chairs) >= int(visitors):
        free_chairs += len(chairs) - int(visitors)
    
    else:
        chairs_sufficient = False
        print(f"{int(visitors) - len(chairs)} more chairs needed in room {room}")

if chairs_sufficient:
    print(f"Game On, {free_chairs} free chairs left")
