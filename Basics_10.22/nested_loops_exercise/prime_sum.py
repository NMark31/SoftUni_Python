optimus_prime = 0
optimus_notprime = 0

while True:
    number = input()

    if number == "stop":
        break

    elif int(number) < 0:
        print(f'Number is negative.')
        continue

    elif int(number) == 0:
        optimus_notprime += int(number)
        continue

    for i in range(2, int(number)):
        if int(number) % i == 0:
            optimus_notprime += int(number)
            break
            
    else:
        optimus_prime += int(number)
        

print(f'Sum of all prime numbers is: {optimus_prime}\nSum of all non prime numbers is: {optimus_notprime}')
