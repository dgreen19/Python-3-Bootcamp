def insertionSort(arr: list) -> list:
    currentVal = None
    for i in range(len(arr)):
        currentVal = arr[i]
        j = i-1 
        while j >= 0 and arr[j] > currentVal:
            j -= 1
        arr[j+1] = arr[j]
    arr[j+1] = currentVal
    return arr

insertionSort([2,1,9,76,4])