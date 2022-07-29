from functools import lru_cache

@lru_cache(maxsize=1000)
def fibSequence(num: int) -> int:
    if num == 1:
        return 1
    elif num == 2:
        return 1
    elif num > 2:
        return fibSequence(num - 1) + fibSequence(num - 2)

# Print the maximum number of Fibnoacci values
for num in range(1,4):
    print(fibSequence(num))
