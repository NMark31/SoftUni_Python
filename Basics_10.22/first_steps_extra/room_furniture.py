h = float(input()) * 100
w = float(input()) * 100

total_area_raw = w * h 
w -= 100
desks_per_row = w // 70
number_of_rows = h // 120
number_of_workspaces = desks_per_row * number_of_rows - 3

print(number_of_workspaces)
