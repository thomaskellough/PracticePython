"""
This exercise is Part 1 of 4 of the Tic Tac Toe exercise
series. The other exercises are: Part 2, Part 3, and Part 4.
Time for some fake graphics! Let’s say we want to draw game
boards that look like this:
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
This one is 3x3 (like in tic tac toe).
Obviously, they come in many other sizes (8x8 for chess,
19x19 for Go, and many more).    Ask the user what size game
board they want to draw, and draw it for them to the screen
using Python’s print statement.    Remember that in Python
3, printing to the screen is accomplished by
print("Thing to show on screen")  Hint: this requires some
use of functions, as were discussed previously on this blog
and elsewhere on the Internet, like this TutorialsPoint
link.
"""
import re


def print_board(width, length):
    for w in range(length):
        print(' --- ' * width)
        for l in range(width + 1):
            print('|    ', end='')
        print()
    print(' --- ' * width)


regex = re.compile(r'^(\d+)x(\d+)$')
while True:
    size = input('What size do you want your board?\nEnter it (num)x(num)\n')
    if not regex.search(size):
        print('Try again')
    else:
        break


width = int(regex.search(size).group(1))
length = int(regex.search(size).group(2))

print_board(width, length)