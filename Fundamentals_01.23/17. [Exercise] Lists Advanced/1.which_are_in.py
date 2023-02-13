list1 = input().split(", ")
list2 = input().split(", ")

result_list = [x for x in list1 if any(x in y for y in list2)]

print(result_list)
