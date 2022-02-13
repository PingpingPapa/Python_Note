n = int(input())

coin = [500, 100, 50, 10]
coin_num = 0
for c in coin:
    coin_num += n // c
    n %= c

print(coin_num)
