first_list = [1,2,3,4,5,6,7,8,9,10]
print (first_list) 
print ("Numbers cut from list:") 
print (first_list [1:3])



f = lambda n:1 if n <= 1 else n * f(n-1)
g = f(4)
print(g)

words = ['Hello', 'World']

for i, word in enumerate(words):
    word.lower()
    words[i] = word[::-1]

print(words)

nums = [0, -1, -2]

def has_pos_neg(nums):
    has_pos = False
    has_neg = False
    for num in nums:
        has_pos = num > 0
        has_neg = num < 0
    return (has_pos, has_neg)

def _(func, items):
    i = 0
    for item in items:
        if func(item):
            items[i] = item
            i += 1
    del items[i:]

