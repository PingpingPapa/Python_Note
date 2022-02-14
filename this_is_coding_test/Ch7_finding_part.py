def binary_search(array, start, end, target):
    mid = (start+end)//2

    if start>=end:
        if array[mid] == target:
            return "yes"
        else:
            return "no"

    if array[mid] >= target:
        return binary_search(array, start, mid, target)
    else:
        return binary_search(array, mid+1, end, target)

n = int(input())
part_list_raw = list(map(int, input().split()))
m = int(input())
order = list(map(int, input().split()))

part_list = sorted(part_list_raw)
for i in range(len(order)):
    print(binary_search(part_list, 0, len(part_list)-1, order[i]), end=' ')

'''
5
8 3 7 9 2 
3
5 7 9
'''