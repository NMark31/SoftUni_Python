n = int(input())
initial_list = []
filtered_list = []

for _ in range(n):
    number = int(input())
    initial_list.append(number)

criteria = input()

if criteria == "even":
    for i in initial_list:
        if i % 2 == 0:
            filtered_list.append(i)

elif criteria == "odd":
    for i in initial_list:
        if i % 2 != 0:
            filtered_list.append(i)

elif criteria == "positive":
    for i in initial_list:
        if i >= 0:
            filtered_list.append(i)

elif criteria == "negative":
    for i in initial_list:
        if i < 0:
            filtered_list.append(i)

print(filtered_list)

