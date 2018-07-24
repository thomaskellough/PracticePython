"""
This exercise is Part 2 of 4 of the Tic Tac Toe exercise
series. The other exercises are: Part 1, Part 3, and Part 4.
As you may have guessed, we are trying to build up to a full
tic-tac-toe board. However, this is significantly more than
half an hour of coding, so we’re doing it in pieces.

Today, we will simply focus on checking whether someone has
WON a game of Tic Tac Toe, not worrying about how the moves
were made.

Your task this week: given a 3 by 3 list of lists that
represents a Tic Tac Toe game board, tell me whether anyone has won,
and tell me which player won, if any. A Tic Tac Toe win is 3
in a row - either in a row, a column, or a diagonal. Don’t
worry about the case where TWO people have won - assume that
in every board there will only be one winner.
"""


def tic_tac_toe(lists):
    # Check rows
    for row in range(3):
        if len(set(lists[row])) == 1:
            if lists[0] == 0:
                return 'Game not finished. Make your next move.'
            return str(('Player ' + str(lists[0]) + ' won!'))
    # Check columns
    for row in range(3):
        col_list = []
        for col in range(3):
            col_list.append(lists[col][row])
        if len(set(col_list)) == 1:
            if col_list[0] == 0:
                return 'Game not finished. Make your next move.'
            return str('Player ' + str(col_list[0]) + ' won!')
    # Check diagonal (top left to bottom right)
    count = -1
    diag_list = []
    for row in range(3):
        count += 1
        diag_list.append(lists[count][row])
    if len(set(diag_list)) == 1:
        if diag_list[0] == 0:
            return 'Game not finished. Make your next move.'
        return str('Player ' + str(diag_list[0]) + ' won!')
    # Check diagonal (top right to bottom left)
    count = 3
    diag_list = []
    for row in range(3):
        count -= 1
        diag_list.append(lists[count][row])
    if len(set(diag_list)) == 1:
        if diag_list[0] == 0:
            return 'Game not finished. Make your next move.'
        return str('Player ' + str(diag_list[0]) + ' won!')
    return str('Sorry, no one won this game.')

