n = int(input())
lst = list(map(int, input().split()))
lst.sort()

cnt = 0
while len(lst) != 0:
    if len(lst) < lst[-1]:
        cnt += 1
        break

    for _ in range(lst[-1]):
        lst.pop()
    cnt+=1
print(cnt)
