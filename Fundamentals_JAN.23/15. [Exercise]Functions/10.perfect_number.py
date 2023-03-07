def is_perfect(num):
    sum_of_divisors = 0

    for n in range(1, num):
        if num % n == 0:
            sum_of_divisors += n

    return sum_of_divisors == num


number = int(input())

if is_perfect(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
