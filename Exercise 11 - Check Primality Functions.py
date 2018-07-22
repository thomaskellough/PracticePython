"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors).
You can (and should!) use your answer to Exercise 4 to help you.
"""

your_number = int(input('Give me a number.\n'))



def prime(number):
    count = 0
    for num in range(1, number):
        if number % num == 0:
            count += 1
    if count > 1:
        return 'Your number is not prime'
    else:
        return 'Your number is prime'


print(prime(your_number))
