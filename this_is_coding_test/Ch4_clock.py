n = int(input())
a = 60 * 60 - 45 * 45
b = 60 * 60

if n < 3:
    print(a*(1+n))
elif n < 13:
    print(a*n + b)
elif n < 23:
    print(a*(n-1) + b * 2)
else:
    print(a*(n-2)+b*3)
