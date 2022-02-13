n, m = map(int, input().split())
cards = []
min = []
for i in range(n):
    cards.append(list(map(int, input().split())))
    cards[i].sort()
    min.append(cards[i][0])

min.sort(reverse = True)
print(min[0])

