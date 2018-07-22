"""
Create a program that asks the user to enter their name and their age. Print out a message
addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out
that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string
"\n is the same as pressing the ENTER button)
"""

name = input('What is your name?\n')
age = int(input('What is your age?\n'))
year = 2018
year_turn_100 = (year - age) + 100
sentence = 'You will turn 100 in year ' + str(year_turn_100)
print(sentence)

number = int(input('Please give me another number.\n'))
print((sentence + '\n') * number)
