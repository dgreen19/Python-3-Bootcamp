from random import choice

# Food Classifying Exercise from Udemy course
food = choice(['apple', 'grape', 'bacon', 'steak', 'worm', 'dirt'])

# CODE MAKES SENSE LOGICALLY FOR OUTCOMES, BUT DOES NOT PASS ALL TEST CASES??? FEATURE OF PYTHON CALLED SHORT-CIRCUITING?
if food == 'apple' or 'grape':
    print(food)
    print('fruit')
elif food == 'bacon' or 'steak':
    print(food)
    print('meat')
else:
    print(food)
    print('yuck')
