x = int(input())
d = [0] * (1+x)
d[1] = 0
print(d)
for i in range(2, x+1):
    add = []

    if i % 5 == 0:
        add.append(d[i//5] + 1)
    if i % 3 == 0:
        add.append(d[i//3] + 1)
    if i % 2 == 0:
        add.append(d[i//2] + 1)

    add.append(d[i-1] + 1)

    d[i] = min(add)

print(d)
print(d[x])