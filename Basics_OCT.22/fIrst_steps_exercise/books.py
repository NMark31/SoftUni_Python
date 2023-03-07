# Input
pages = int(input())
pages_per_hour = int(input())
days = int(input())

# Logic

total_hours = pages / pages_per_hour / days

# Output
print(int(total_hours))