"""
Take the code from the How To Decode A Website exercise
(if you didn’t do it or just want to play with some different code,
use the code from the solution), and instead of printing the results
to a screen, write the results to a txt file. In your code, just make
up a name for the file you are saving to.

Extras:

Ask the user to specify the name of the output file that will be saved.
"""

import requests
import bs4
import textwrap


url = 'https://en.wikipedia.org/wiki/Spider-Man'
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')


elems = soup.findAll(id='bodyContent')

for elem in range(len(elems)):
    elem_list = textwrap.wrap(elems[elem].getText(), 80)

name = input('What do you want to name your text file?\n')

with open(name, 'wb') as f:
    elem_string = '\n'.join(str(x) for x in elem_list)
    f.write(elem_string.encode('utf-8'))
