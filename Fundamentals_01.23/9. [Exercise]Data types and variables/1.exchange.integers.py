a = int(input())
b = int(input())

print(f"Before: \na = {a}\nb = {b}")

temp_var = a
a = b
b = temp_var

print(f"After: \na = {a}\nb = {b}")
