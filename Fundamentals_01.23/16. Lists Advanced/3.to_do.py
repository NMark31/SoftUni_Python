to_do_list = []
tens = []
while True:
    item = input()

    if item == "End":
        break
    else:
        to_do_list.append(item)

for element in to_do_list:
    args = element.split("-")
    if int(args[0]) > 9:
        tens.append(args[1])
        to_do_list.remove(element)

to_do_list.sort()
tens.sort()
to_do_list = [list_item[list_item.find("-") + 1:] for list_item in to_do_list] + tens
print(to_do_list)
