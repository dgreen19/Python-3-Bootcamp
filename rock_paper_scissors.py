from random import choice
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