def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        small = []
        big = []
        for el in arr:
            if el < pivot:
                small.append(el)
            else: 
                big.append(el)
        return (quicksort(small) + [pivot] + quicksort(big))

unsorted = [5,4,7,8,9,1,4,3,10,12]
sorted = quicksort(unsorted)
print(sorted)
