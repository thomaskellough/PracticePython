"""
Write a password generator in Python. Be creative with how you generate
passwords - strong passwords have a mix of lowercase letters, uppercase
letters, numbers, and symbols. The passwords should be random, generating
a new password every time the user asks for a new password.
Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords,
pick a word or two from a list.
"""

import random
import string


strong_length = random.randint(9, 15)
medium_length = random.randint(5, 8)
length_dict = {'strong': random.randint(11, 20),
               'medium': random.randint(6, 10),
               'weak': ['rosebud', 'swordfish', 'klapaucius', 'qwertyuiop']}
password = []

while True:
    strength = input('Do you want a weak, medium, or strong password?\n')
    if strength in ('weak', 'medium', 'strong'):
        break
    print("Please type either 'weak', 'medium', or 'strong'.")


def random_choice():
    letter = random.choice(string.ascii_letters)
    digit = random.randint(0, 9)
    punctuation = random.choice(string.punctuation)
    char = [letter, digit, punctuation]
    return random.choice(char)


def generate_password(strength):
    for k, v in length_dict.items():
        if strength != k:
            pass
        else:
            if k == 'weak':
                return random.choice(v)
            else:
                for i in range(v):
                    x = random_choice()
                    password.append(x)
                return ''.join(str(x) for x in password)

print(generate_password(strength))

