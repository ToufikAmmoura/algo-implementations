def swap(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def isSorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def bubble(arr, end):
    index = 0 
    while index <= end:
        if arr[index] > arr[index+1]:
            swap(index, index+1, arr)
        index += 1 

def bubbleSort(arr):
    end = len(arr)-2
    while not isSorted(arr):
        bubble(arr, end)
        end -= 1

arr = [5,4,7,8,9,1,4,3,10,12]
bubbleSort(arr)
print(arr)
