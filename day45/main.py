# day 45
import requests
from mylib.cache import CacheFile
from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://appbrewery.github.io/news.ycombinator.com/'
cache_file = 'tmp/appbrewery.news.ycombinator.html'

cache = CacheFile(cache_file)
if cache.is_cached():
    html = cache.get()
else:
    resp = requests.get(url)
    html = resp.text
    cache.save(html)

#print(html)

soup = BeautifulSoup(html, 'html.parser')


# get all the scores on the sheet.
scores_found = soup.select('span .score')

# as we go through each one... lets find the winner.
highest_score = 0
winner_id = 0
for score in scores_found:
    # funky casting..
    score_value = int(score.getText().split(' ')[0])
    if score_value > highest_score:
        id_value = str(score.get('id'))
        winner_id = int(id_value[6:])

print('Winner is', winner_id)

# get the table row that has the information.
winner = soup.find(name="tr", class_="athing", id=f"{winner_id}")
a_tag = winner.select_one('a.storylink')

print("The Winner:")
print("\t", a_tag.getText())
print("\t", a_tag.get('href'))



