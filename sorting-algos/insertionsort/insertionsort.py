def isSorted(arr):
    for index in range(len(arr)-1):
        if arr[index] > arr[index+1]:
            return False
    return True

def insert(arr, index):
    el = arr.pop(index)
    i = 0
    while i < index:
        if el <= arr[i]:
            arr.insert(i, el)
            return
        i+=1
    arr.insert(index, el)

def insertionsort(arr):
    i = 1
    while not isSorted(arr) and i < len(arr):
        insert(arr, i)
        i+=1

arr = [5,4,7,8,9,1,4,3,10,12]
insertionsort(arr)
print(arr)