# Input
deposit = float(input())
deadline = int(input())
interest = float(input()) / 100

# Logic
total = deposit + deadline * ((deposit * interest) / 12)

# Output 
print(total)
