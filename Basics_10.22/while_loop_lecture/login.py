username = input()
password = input()

while True:
    credentials = input()

    if credentials == password:
        print(f"Welcome {username}!")
        break
    