number = input()

separated_digits = [number[i] for i in range(len(number))] #string list

str_to_int = [eval(j) for j in separated_digits] #integer list

str_to_int.sort(reverse=True)

for d in str_to_int:
    print(d, end="")
