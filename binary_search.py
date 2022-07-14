"""GENERIC BINARY SEARCH ALGORITHM"""

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo +hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1 #MOVE LEFT FROM THE MIDPOINT
        else:
            lo = mid + 1
        return - 1

def binary_search(array) -> int:
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
        
        
