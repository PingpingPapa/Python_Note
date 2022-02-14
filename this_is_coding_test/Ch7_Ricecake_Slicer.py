n, m= map(int, input().split())
lst = list(map(int, input().split()))

def slicer(lst, cutter):
    sum = 0
    for i in lst:
        if i > cutter:
            sum += i - cutter

    return sum

def f1(lst, m):
    t = max(lst)
    while slicer(lst, t) < m:
        t -= 1

    return t

print(f1(lst, m))
'''
4 6
19 15 10 17
'''