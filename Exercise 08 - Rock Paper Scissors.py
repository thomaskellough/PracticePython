"""
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and
ask if the players want to start a new game)
"""

again = ' '
while again is not '':
    player_1 = ''
    player_2 = ''
    while player_1 not in ['rock', 'paper', 'scissors']:
        player_1 = input('Player 1: Rock, paper or scissors?\n')
    while player_2 not in ['rock', 'paper', 'scissors']:
        player_2 = input('Player 2: Rock, paper or scissors?\n')

    if player_1 == 'rock':
        if player_2 == 'rock':
            print('Tie!')
        elif player_2 == 'paper':
            print('Player 2 wins!')
        else:
            print('Player 1 wins!')

    elif player_1 == 'paper':
        if player_2 == 'paper':
            print('Tie!')
        elif player_2 == 'rock':
            print('Player 1 wins!')
        else:
            print('Player 2 wins!')

    else:
        if player_2 == 'scissors':
            print('Tie!')
        elif player_2 == 'rock':
            print('Player 2 wins!')
        elif player_2 == 'paper':
            print('Player 1 wins!')
    again = input('Would you like to play again? Press enter to quit.\n')
