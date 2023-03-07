# In
length = int(input())
width = int(input())
height = int(input())
percent_filled = float(input()) / 100

# Logic

total_volume = (length * width * height) / 1000
sediment = total_volume * percent_filled
water_volume = total_volume - sediment

# Out
print(water_volume)