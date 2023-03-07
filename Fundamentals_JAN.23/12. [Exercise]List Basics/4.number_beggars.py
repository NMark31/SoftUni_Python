market = input().split(", ")
market = [int(i) for i in market]

beggars = int(input())
result_list = [0] * beggars

for _ in range(len(market)):
    for b in range(beggars):
        if not market:
            break
        result_list[b] += market[0]
        market.pop(0)

print(result_list)

