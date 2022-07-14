"""Frequency COunter Algorithm naive approach"""
list1 = [1,2,3,2]
list2 = [9,1,4,4]

def same(list1,list2):
# Check if length of array 1 matches array 2
    if len(list1) != len(list2):
        return False
# Loop over the entirety of the array
    for i in list1: 
        if i < len(list1):
            i+= 1
            correctIndex = list2.index(list1[i] ** 2)
            if correctIndex == -1:
                return False
            print(list2)
            list2.remove(correctIndex,1)
    return True    
