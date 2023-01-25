integer_list = [8, 3, 3, 16]
string_list = []

for i in integer_list:
    string_list.append(str(i))

joined_string = "".join(string_list)
print(int(joined_string))

