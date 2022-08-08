"""SEARCHING AND SORTING ALGORITHMS"""

"""LINEAR SEARCH Time Complexity of O(n)!"""
def linearSearch(arr: list, val):
    for i in range(len(arr)):
       if arr[i] == val:
           return i
    return -1

linearSearch([34,51,1,2,3,45,56,687], 100)

"""BINARY SEARCH must be sorted before you can use it!!!"""
def binarySearch(arr: list, val):
    arr.sort
    

