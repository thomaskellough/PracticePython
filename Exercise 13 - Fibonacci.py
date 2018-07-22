"""
Write a program that asks the user how many Fibonnaci numbers to generate and then
generates them. Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the
sequence is the sum of the previous two numbers in the sequence. The sequence looks
like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

num = int(input('How many Fibonnaci numbers do you want to generate?\n'))

fib_list = [1]
first = [1]


def fibonacci(number):
    for number in range(1, number - 1):
        fib_number = fib_list[number - 1] + fib_list[number - 2]
        fib_list.append(fib_number)
    return first + fib_list


print(fibonacci(num))
