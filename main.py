import random

computerList = ['Rock','Paper','Scissors']

computerC = (random.choice(computerList))

humanC = input("What's your move?:\n"
               "1- Rock\n"
               "2- Paper\n"
               "3- Scissors")

if humanC == 'Rock' and computerC == 'Paper':
    print('You lose')
elif humanC == 'Rock' and computerC == 'Scissors':
    print('You win')
elif humanC == 'Paper' and computerC == 'Rock':
    print('You Win')
elif humanC == 'Paper' and computerC == 'Scissors':
    print('You Lose')
elif humanC == 'Scissors' and computerC == 'Rock':
    print('You Lose')
elif humanC == 'Scissors' and computerC == 'Paper':
    print('You Win')
else:
    print('Draw')