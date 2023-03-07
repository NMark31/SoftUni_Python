# Input
town = input()
sales = float(input())

# Logic
commission = 0

if town == 'Sofia':
    if 0 <= sales <= 500:
        commission = 0.05
    elif 500 <= sales <= 1000:
        commission = 0.07
    elif 1000 <= sales <= 10000:
        commission = 0.08
    elif sales > 10000:
        commission = 0.12

elif town == 'Varna':
    if 0 <= sales <= 500:
        commission = 0.045
    elif 500 <= sales <= 1000:
        commission = 0.075
    elif 1000 <= sales <= 10000:
        commission = 0.1
    elif sales > 10000:
        commission = 0.13

elif town == 'Plovdiv':
    if 0 <= sales <= 500:
        commission = 0.055
    elif 500 <= sales <= 1000:
        commission = 0.08
    elif 1000 <= sales <= 10000:
        commission = 0.12
    elif sales > 10000:
        commission = 0.145

else:
    commission = -0

if  commission < 0 or sales < 0:
    print('error')
else:
    result = sales * commission
    print(f'{result:.2f}')
