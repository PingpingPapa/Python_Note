n = int(input())
storage = list(map(int, input().split()))

def plund(storage):
    if len(storage) == 1:
        return storage[0]
    elif len(storage) == 2:
        return max(storage)
    else:
        case_1 = storage[0] + plund(storage[2:])
        case_2 = plund(storage[1:])
        return max([case_1, case_2])

print(plund(storage))

'''
5
1 3 1 5 99
'''