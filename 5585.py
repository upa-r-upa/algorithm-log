price = int(input())

change = 1000 - price
coins = [500, 100, 50, 10, 5, 1]
count = 0

for coin in coins:
    coin_count = change // coin
    count += coin_count
    change -= coin_count * coin

print(count)