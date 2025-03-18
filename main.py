import random

computerList = ['Rock','Paper','Scissors']

computerC = (random.choice(computerList))

humanC = input("What's your move?:\n"
               "1- Rock\n"
               "2- Paper\n"
               "3- Scissors")

if humanC.lower() == 'rock' and computerC.lower() == 'paper':
    print('You lose')
elif humanC.lower() == 'rock' and computerC.lower() == 'scissors':
    print('You win')
elif humanC.lower() == 'paper' and computerC.lower() == 'rock':
    print('You Win')
elif humanC.lower() == 'paper' and computerC.lower() == 'scissors':
    print('You Lose')
elif humanC.lower() == 'scissors' and computerC.lower() == 'rock':
    print('You Lose')
elif humanC.lower() == 'scissors' and computerC.lower() == 'paper':
    print('You Win')
else:
    print('Draw')