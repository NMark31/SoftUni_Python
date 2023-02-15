user_input = input().split(", ")
positive = []
negative = []
even = []
odd = []

for x in user_input:
    if int(x) >= 0:
        positive.append(x)
    
    elif int(x) < 0:
        negative.append(x)
    
    if int(x) % 2 == 0:
        even.append(x)
    
    elif int(x) % 2 != 0:
        odd.append(x)
    

print(f'Positive: {", ".join(positive)}')
print(f'Negative: {", ".join(negative)}')
print(f'Even: {", ".join(even)}')
print(f'Odd: {", ".join(odd)}')
