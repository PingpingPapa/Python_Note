array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array2 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = array[start]
    left = start+1
    right = end

    while left <= right:
        print("lleft", left)
        while array[left] <= pivot and left <= end:
            left += 1
        while array[right] >= pivot and start < right:
            right -= 1

        if left>right:
            array[start], array[right] = array[right], array[start]
        else:
            array[left], array[right] = array[right], array[left]
        print("left:{}, right:{}".format(left, right))
        print(array)

    print("one cycle end    {}/{}/{}".format(start, right, end))
    print()
    quick_sort(array, start, right-1)
    quick_sort(array, right + 1, end)

#quick_sort(array,0,len(array)-1)
#print(array)

def quick_sort2(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort2(left) + [pivot] + quick_sort2(right)

print(quick_sort2(array2))