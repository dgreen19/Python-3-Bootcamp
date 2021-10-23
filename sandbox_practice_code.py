# TESTING 'None' types
from random import choice
name = "Daisy"
age = 32
child = None

print("What is the name of the parent and their child?")
print(name)
print(age)
print(child)

type(name)
type(age)
type(child)

# String Formatting/ String Interpolation
x = 10
formatted = f"I've told you about {10} times already!"
print(formatted)

# Other way to interpolate strings!
first = "Darryl"
last = "Green"
formatted = "First Name: {}, Last Name: {}".format(first, last)

# Food Classifying Exercise from Udemy course
food = choice(['apple', 'grape', 'bacon', 'steak', 'worm', 'dirt'])

# CODE MAKES SENSE LOGICALLY FOR OUTCOMES, BUT DOES NOT PASS ALL TEST CASES??? FEATURE OF PYTHON CALLED SHORT-CIRCUITING?
if food == 'apple' or 'grape':
    print('fruit')
elif food == 'bacon' or 'steak':
    print('meat')
else:
    print('yuck')

# Rock, Paper Scissors
rps_game = choice(['rock', 'paper', 'scissors'])
print("Chose rock, paper, or scissors")
rps_input = input()


while rps_input == 'rock' and rps_game == 'rock' or rps_input == 'paper' and rps_game == 'paper' or rps_input == 'scissors' and rps_game == 'scissors':
    print("The other player chose " + rps_game)
    print("Try that again")
    rps_game = choice(['rock', 'paper', 'scissors'])
    print("Chose rock, paper, or scissors")
    rps_input = input()

if rps_input == 'rock' and rps_game == 'paper':
    print("The other player chose " + rps_game)
    print("you lose!")
elif rps_input == 'rock' and rps_game == 'scissors':
    print("The other player chose " + rps_game)
    print("You win!")

if rps_input == 'paper' and rps_game == 'scissors':
    print("The other player chose " + rps_game)
    print("you lose!")
elif rps_input == 'paper' and rps_game == 'rock':
    print("The other player chose " + rps_game)
    print("You win!")

if rps_input == 'scissors' and rps_game == 'rock':
    print("The other player chose " + rps_game)
    print("you lose!")
elif rps_input == 'scissors' and rps_game == 'paper':
    print("The other player chose " + rps_game)
    print("You win!")
