# notes 46
# Musical time machine.
import requests
from bs4 import BeautifulSoup

from lib46.cache_file import cache_file
from mylib.cache import CacheFile

from pprint import pprint


url = 'https://www.billboard.com/charts/hot-100/2000-08-12'
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
file = cache_file(url=url, name='hot-100.2000-08.12', type='html')
main_cache = CacheFile(file)
if main_cache.is_cached():
    html = main_cache.get()
else:
    resp = requests.get(url, headers=header)
    # make it a little more readable.
    html = BeautifulSoup(resp.text, 'html.parser').prettify()
    main_cache.save(html)

soup = BeautifulSoup(html, 'html.parser')

# yeah scraping sites can get ugly.
divs = soup.select(selector='div .o-chart-results-list-row-container')
for div in divs:
    record = BeautifulSoup(str(div), 'html.parser')
    song = record.select_one(selector='ul li h3').text.strip()
    rank = record.select(selector='ul li span')[0].text.strip()
    artist = record.select(selector='ul li span')[1].text.strip()
    if artist == 'NEW':
        # there are two NEW items
        artist = record.select(selector='ul li span')[3].text.strip()
    # best to do this with regex, but this is good enough for now.
    artist = artist.replace("\n"+" "*20, ' ').replace('  ', ' ')


    print(f"{rank}: '{song}' by [{artist}]")


