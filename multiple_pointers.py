def sumZero(list1:int) -> bool:
    list1.sort()
   
   left = 0
   right = len(list1) -1
   
   while (left < right):
       sum = list1[left] + list1[right]
       if (sum == 0):
           return [list1[left], list1[right]]
       