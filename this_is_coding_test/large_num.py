n, m, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

l1 = lst[n-1]
l2 = lst[n-2]

result = (l1*k+l2) * (m // (k+1)) + l1*(m%(k+1))
print(result)
