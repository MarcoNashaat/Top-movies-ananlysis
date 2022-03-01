#enabling https
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#importing libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

#getting info about top 250 imdb movies
html = urlopen('https://www.imdb.com/chart/top/')
bs = BeautifulSoup(html,'html.parser')

data = []

for movie in bs.find_all('td',{'class':'titleColumn'}):
    row = {'title':movie.find('a').text,
           'year':movie.find('span').text[1:-1],
           'rating':movie.next_sibling.next_sibling.find('strong').text}
    data.append(row)

df = pd.DataFrame(data)
df.to_csv(index=False)

