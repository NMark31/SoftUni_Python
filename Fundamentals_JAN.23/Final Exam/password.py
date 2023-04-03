import re


n = int(input())

regex = r"(.+)>(?P<password>[0-9]{3}\|[a-z]{3}\|[A-Z]{3}\|.{3})<(\1)"

matches = []

for _ in range(n):
    password = input()

    if not re.search(regex, password):
        print("Try another password!")

    elif re.search(regex, password):
        encrypted_password = re.finditer(regex, password)
        for pwd in encrypted_password:
            encrypted = pwd.group("password")
            encrypted = encrypted.split("|")
            print(f"Password: {''.join(encrypted)}")
