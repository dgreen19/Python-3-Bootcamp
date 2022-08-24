
"""ARRAYS NEED TO BE ALREADY SORTED BEFORE MERGE!"""
def mergeArrays(arr1, arr2) -> list:
    results = []
    # Starting pointer in Array 1
    i = 0
    # Starting pointer in Array 2
    j = 0
    while i < len(arr1) and j < len(arr2):
        if(arr2[j] >= arr1[i]):
            results.append(arr1[i])
            i += 1
        else:
            results.append(arr2[j])
            j+=1
    while i < len(arr1): 
        results.append(arr1[i])
        print(arr1[i])
        i+=1
        
            
    while j < len(arr2):
        results.append(arr2[j])
        print(arr2[j])
        j+=1
        
        
    print(arr1)
    print(arr2)
    return results

# print(mergeArrays([100,200], [1,2,3,5,6]))

def mergeSort(arr: list) -> list:
    if len(arr) <= 1:
        return arr
    mid = round(len(arr)/2)
    left = mergeSort(arr.slice(0,mid))
    right = mergeSort(arr.slice(mid))
    return mergeArrays(left, right)

print(mergeSort([1,2,4,7,100,234,119,5,8,222]))
    