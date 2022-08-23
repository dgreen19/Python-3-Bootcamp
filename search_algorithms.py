"""SEARCHING AND SORTING ALGORITHMS"""

"""LINEAR SEARCH Time Complexity of O(n)!"""
def linearSearch(arr: list, val) -> int:
    for i in range(len(arr)):
        print(val)
        if arr[i] == val:
           return i
    return -1

linearSearch([34,51,1,2,3,45,56,687], 100)

"""BINARY SEARCH must be sorted before you can use it!!!"""
def binarySearch(arr:list, elem) -> int:
    startIdx = 0
    endIdx = len(arr) - 1
    midIdx = (startIdx + endIdx) // 2
    while arr[midIdx] != elem and startIdx <= endIdx: 
        print(startIdx, midIdx, endIdx)
        if elem < arr[midIdx]:
            endIdx = midIdx - 1
        else: 
            startIdx = midIdx + 1
        midIdx = (startIdx + endIdx) // 2
    print(startIdx, midIdx, endIdx)
    if arr[midIdx] == elem:
        return midIdx
    else:
        return -1
        
    
binarySearch([2, 5, 6, 9, 13, 15, 28, 30], 15)

"""NAIVE STRING SEARCH"""
def stringSearch(longStr, shortStr) -> str:
    for  i in range(len(longStr)):
        for j in range(len(shortStr)):
            if shortStr[j] != longStr[i+j]:
                break
            print(longStr[i], shortStr[j])

stringSearch("lori loled", "lol")