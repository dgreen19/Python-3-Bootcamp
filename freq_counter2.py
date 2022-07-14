def same(list1: int, list2: int) -> bool:
    print(list1)
    print(list2)
    # Check if length of array 1 matches array 2
    if len(list1) != len(list2):
        return False
    frequencyCount1 = {}
    frequencyCount2 = {}
    for item in list1:
        if item in frequencyCount1:
            frequencyCount1[item] += 1
        else:
            frequencyCount1[item] = 1

    for item in list2:
        if item in frequencyCount2:
            frequencyCount2[item] += 1
        else:
            frequencyCount2[item] = 1

    print(frequencyCount1)
    print(frequencyCount2)
    for key, value in frequencyCount1.items():
        if (not (key ** 2 in frequencyCount2)):
            return False
        if (frequencyCount2[key ** 2] is not frequencyCount1[key]):
            return False

    return True
