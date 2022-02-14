def binary_search(array, start, end, target):
    mid = (start+end)//2
    if start >= end:
        if array[mid] == target:
            return mid
        else:
            return "No Target"


    if array[mid]>=target:
        return binary_search(array, start, mid, target)
    else:
        return binary_search(array, mid+1, end, target)

array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

print(binary_search(array, 0, len(array)-1, 7))