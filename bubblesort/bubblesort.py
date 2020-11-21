def swap(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def isSorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def bubble(arr):
    el = arr[0]
    for i in range(len(arr)-1):    
        if el > arr[i+1] 
            

def bubbleSort(arr):
