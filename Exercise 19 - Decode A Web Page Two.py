"""
Using the requests and BeautifulSoup Python libraries, print to the screen the
full text of the article on this website:
http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print
out the text to the screen so that you can read the full article without
having to click any buttons.

(Hint: The post here describes in detail how to use the BeautifulSoup and
requests libraries through the solution of the exercise posted here.)

This will just print the full text of the article to the screen. It will
not make it easy to read, so next exercise we will learn how to write this
text to a .txt file.
"""

import bs4
import requests
import textwrap

url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')


def print_text(elem):
    for i in range(len(elem)):
        text = textwrap.wrap(elem[i].getText(), width=80)
        for line in text:
            print(line)


intro_elem = soup.findAll('div', class_='dek')
content_elem = soup.findAll('section', class_='content-section')

print_text(intro_elem)
print_text(content_elem)
