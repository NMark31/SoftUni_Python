number = float(input())
sign = ""

if number == 0:
    print("zero")

elif number > 0:
    sign = "positive"
    if 0 < abs(number) < 1:
        print("small " + sign)

    elif abs(number) > 100000:
        print("large " + sign)

    else:
        print(sign)

else:
    sign = "negative"
    if 0 < abs(number) < 1:
        print("small " + sign)

    elif abs(number) > 100000:
        print("large " + sign)

    else:
        print(sign)


