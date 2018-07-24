import logging

logging.basicConfig(filename='tictactoe.log', level=logging.DEBUG,
                    format='%(asctime)s	- %(levelname)s	- %(message)s: ')

game_board = [[' ', ' ', ' '],
              [' ', ' ', ' '],
              [' ', ' ', ' ']]

count = 1
coordinates_list = []


def print_board():
    for row in game_board:
        print(row)


def play():
    global count
    player_1 = 'X'
    player_2 = 'O'
    try:
        coordinates = input('Please enter where you want to play (row, col)\n').split(',')
        logging.debug(str(coordinates) + ' entered.')
        if coordinates not in coordinates_list:
            logging.debug(str(coordinates) + ' are new.')
            coordinates_list.append(coordinates)
        else:
            logging.debug(str(coordinates) + ' are repeated.')
            count -= 1
            print_board()
            return print('You cannot play there. Try a space that is available')
        row = int(coordinates[0].strip())
        col = int(coordinates[1].strip())
        if count % 2 != 0:
            game_board[row - 1][col - 1] = player_1
        else:
            game_board[row - 1][col - 1] = player_2
        print_board()
    except IndexError:
        logging.debug('Index Error: coordinates out of range')
        print('Please enter a coordinate on the board.')
        print_board()
        play()


while count < 10:
    play()
    count += 1
