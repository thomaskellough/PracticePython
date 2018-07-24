"""
Given two .txt files that have lists of numbers in them, find the numbers that
are overlapping. One .txt file has a list of all prime numbers under 1000,
and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other number.
And yes, happy numbers are a real thing in mathematics - you can look it up on
Wikipedia. The explanation is easier with an example, which I will describe below.)
"""

prime_text = open('primelist.txt')
prime_list = []
for prime in prime_text:
    prime = prime.replace('\n', '')
    prime_list.append(int(prime))

happy_text = open('happylist.txt')
happy_list = []
for happy in happy_text:
    happy = happy.replace('\n', '')
    happy_list.append(int(happy))

print(sorted(set(prime_list) & set(happy_list)))
