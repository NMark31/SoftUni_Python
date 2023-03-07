# In 
yearly_sub = int(input())

# Prices
sneakers = yearly_sub * 0.6
jersey = sneakers * 0.8
ball = jersey / 4
accessories = ball / 5

# Logic

total_price = yearly_sub + sneakers + jersey + ball + accessories

# Out
print(total_price)