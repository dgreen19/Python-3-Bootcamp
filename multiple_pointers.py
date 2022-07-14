def sumZero(list1: int):
    # Starting left point at index at 0
    left = 0
    # Starting right pointer at last index in list/array
    right = len(list1) - 1

    while (left < right):
        sum = list1[left] + list1[right]
        if (sum == 0):
            print(list1[left], list1[right])
            return [list1[left], list1[right]]
        elif sum > 0:
            # Decrement the right pointer by 1 if number is greater than 0
            right -= 1
    # Increment the left pointer by 1 if number isn't greater than 0
        else:
            left += 1


sumZero([-12, -4, -3, -2, -1, 0, 1, 6, 5, 12])


def countUniqueValues(numList: int):
    i = 0
    for j in numList:
        # while j < len(numList):
        j += 1
        print(i,j)
    if numList[i] != numList[j]:
        i += 1
        numList[i] = numList[j]
        print(numList)


countUniqueValues([1, 2, 2, 2, 2, 2, 3, 3, 4, 4, 5, 6, 6, 6, 7, 8])
