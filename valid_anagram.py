def validAnagram(str1, str2) -> bool:
    print(str1)
    print(str2)
    # Check if length of string 1 matches string 2
    if len(str1) != len(str2):
            return False

    dictStr1, dictStr2 = {}, {}
        
    for i in range(len(str1)):
        dictStr1[str1[i]] = 1 + dictStr1.get(str1[i], 0)
        dictStr2[str2[i]] = 1 + dictStr2.get(str2[i], 0)
    for c in dictStr1:
        if dictStr1[c] != dictStr2.get(c, 0):
            return False
    return True
    
validAnagram('anagram', 'nagaram')
    
    
