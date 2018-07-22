"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""

a = [5, 10, 15, 20, 25]
b = [43, 1, 223, 345, 3, 6, 24, 56]

def first_last(list):
    new_list = []
    new_list = [list[0], list[-1]]
    return new_list

print(first_last(a))
print(first_last(b))
