"""
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. Hint: how does an even / odd
number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one
number to divide by (check). If check divides evenly into num, tell that to the user.
If not, print a different appropriate message.
"""

number = int(input('Give me a number.\n'))

if number % 4 is 0:
    print('Your number is divisible by 4')
elif number % 2 is 0:
    print('Your number is even')
else:
    print('Your number is odd')

dividend = int(input('Give me a dividend.\n'))
divisor = int(input('Give me a divisor.\n'))
if dividend % divisor is 0:
    print(str(dividend) + ' a multiple of ' + str(divisor))
else:
    print(str(dividend) + ' does not divide evenly into ' + str(divisor))
