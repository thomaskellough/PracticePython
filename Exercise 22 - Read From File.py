"""
Given a .txt file that has a list of a bunch of names, count how many of each
name there are in the file, and print out the results to the screen. I have
a .txt file for you, if you want to use it!

Extra:

Instead of using the .txt file from above (or instead of, if you want the challenge),
take this .txt file, and count how many of each “category” of each image there are.
This text file is actually a list of files corresponding to the SUN database
scene recognition database, and lists the file directory hierarchy for the images.
Once you take a look at the first line or two of the file, it will be clear which
part represents the scene category. To do this, you’re going to have to remember
a bit about string parsing in Python 3. I talked a little bit about it in this post.
"""

import random
import re

# Create a texdt file with a list of names
"""
names = ['Harry Potter', 'Hagrid', 'Severus Snape', 'Hermione Granger', 'Ronald Weasley']
names_list = []
for i in range(100):
    name = random.choice(names)
    names_list.append(name)
for name in names_list:
    with open('HPnames.txt', 'a') as f:
        f.write(name + '\n')
"""

names = open('HPnames.txt')


names_dic = {}

for name in names.readlines():
    name = name.replace('\n', '')
    if name in names_dic:
        names_dic[name] += 1
    else:
        names_dic[name] = 1

print(names_dic)
names.close()

# Using the text file provided
regex = re.compile(r'(/\w)(.+/)(.*)')

images = open('exercise22text.txt')
image_dict = {}
for image in images.readlines():
    image = image.replace('\n', '')
    mo = regex.search(image)
    #print(image)
    if mo:
        category = mo.group(2)
        category = category.replace('/', '')
        if category in image_dict:
            image_dict[category] += 1
        else:
            image_dict[category] = 1
    else:
        print('No file')
print(image_dict)
images.close()