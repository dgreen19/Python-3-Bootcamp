"""GENERIC BINARY SEARCH ALGORITHM"""

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo+hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1 #MOVE LEFT FROM THE MIDPOINT
        else:
            lo = mid + 1 #MOVE RIGHT FROM THE MIDPOINT
        return - 1

def binary_search(array: list) -> int:
    def condition(value) -> bool:
        pass
    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
            return left
        
def binarySearch(arr:list, elem):
    start = 0
    end = len(arr) - 1
    mid = (start + end) // 2
    while arr[mid] != elem and start <= end: 
        print(start, mid, end)
        if elem < arr[mid]:
            end = mid - 1
        else: 
            start = mid + 1
        mid = (start + end) // 2
    print(start, mid, end)
    if arr[mid] == elem:
        return mid
    else:
        return -1
        
    
binarySearch([2, 5, 6, 9, 13, 15, 28, 30], 15)
    
        
        
