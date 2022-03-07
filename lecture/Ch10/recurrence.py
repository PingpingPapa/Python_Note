def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def downup(word):
    print(word)
    if len(word)>2:
        downup(word[:-1])
    print(word[:-1])

def num_sys(nn):
    n = int(nn)
    if n>2:
        num_sys(n//2)

    print(n % 2, end='')

def merge_sort(a):
    print(a)
    if len(a) <= 1:
        return a
    m = len(a)//2
    a1 = a[:m]
    a2 = a[m:]
    l = merge_sort(a1)
    r = merge_sort(a2)
    lst = merge(l, r)

    return lst

def merge(left, right):
    print("merge", left, right)
    lst = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            lst.append(left[l])
            l += 1

        else:
            lst.append(right[r])
            r += 1

    lst += left[l:]
    lst += right[r:]
    print("result", lst)
    return lst

lk = [5, 46, 54 ,21 ,4, 24, 1, 21, 6, 1 ,10 ,5 ,5 ,99]
print(merge_sort(lk))
'''
1 5 7 // 2 6 15
3 1 1 
1 1 0

'''