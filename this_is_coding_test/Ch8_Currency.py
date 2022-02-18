n, m = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

#efficient_currency_compose
def ecc(coins, m):
    if m <= max(coins):
        if not m in coins:
            return -1
        else:
            return 1

    best_coin = coins[0]
    for coin in coins:
        if ecc(coins, m-best_coin) == -1:
            best_coin = coin
        elif ecc(coins, m-coin) != -1 and (ecc(coins, m-coin) < ecc(coins, m-best_coin)):
            best_coin = coin
        else:
            pass

    if ecc(coins, m-best_coin) == -1:
        return -1
    else:
        return ecc(coins, m-best_coin)+1

print(ecc(coins, m))
'''
2 15
2
3

3 4
3
5
7

'''

