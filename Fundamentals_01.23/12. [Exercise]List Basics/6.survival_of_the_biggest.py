list_of_numbers = input().split()
to_remove = int(input())

list_of_numbers = [int(i) for i in list_of_numbers]

for _ in range(to_remove):
    list_of_numbers.remove(min(list_of_numbers))


list_of_numbers = [str(j) for j in list_of_numbers]
print(", ".join(list_of_numbers))
