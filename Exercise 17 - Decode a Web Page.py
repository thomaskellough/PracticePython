"""
Use the BeautifulSoup and requests Python packages to print out a list of all the
article titles on the New York Times homepage.
"""

import bs4
import requests

url = 'https://www.nytimes.com/'

res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

tags = soup.findAll('a', {'class': 'story-link'})

for link in range(len(tags)):
    print(tags[link].get('href'))



