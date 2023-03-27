import re

n = int(input()) # number of barcodes
regex = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
regex_digits = r"\d"

for _ in range(n):
    matches = []
    match_digits = []

    line = input()

    matches = re.findall(regex, line)

    if not matches:
        print("Invalid barcode")
        continue
    
    match_digits = re.findall(regex_digits, line)
    if match_digits:
        print(f"Product group: {''.join(match_digits)}")
    else:
        print("Product group: 00")
    

