"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

string = input('Input a string\n')
backwards_string = ''.join([string[::-1]])

if string == backwards_string:
    print('Your string is a palindrome')
else:
    print('Your string is not a palindrome')
