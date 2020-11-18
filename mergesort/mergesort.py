from math import inf

def merge(arr1, arr2):
    merged = []
    arr1.append(inf)
    arr2.append(inf)
    index1 = index2 = 0
    while 1:
        el1 = arr1[index1]
        el2 = arr2[index2]
        if el1 == inf:
            merged = merged + arr2[index2:-1]
            break
        elif el2 == inf:
            merged = merged + arr1[index1:-1]
            break
        elif el1 < el2:
            merged.append(el1)
            index1 += 1
        else:
            merged.append(el2)
            index2 += 1
    return merged


def mergesort(arr):
    if len(arr) <= 1:
        return arr
    else:
        center = len(arr)//2
        begin = mergesort(arr[:center])
        end = mergesort(arr[center:])
        return merge(begin, end)

unsorted = [5,4,7,8,9,1,4,3,10,12]
sorted = mergesort(unsorted)
print(sorted)
