"""
Write a program (function!) that takes a list and returns a new list that contains all
the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing
a list, and another using sets.
"""

colors = ['red', 'red', 'purple', 'blue', 'red', 'purple', 'yellow', 'blue', 'orange']


def remove_duplicates(list):
    new_list = []
    for element in list:
        if element in new_list:
            continue
        else:
            new_list.append(element)
    return new_list


def remove_duplicate_2(list):
    new_list = set(colors)
    return new_list


print(remove_duplicates(colors))
print(remove_duplicate_2(colors))
