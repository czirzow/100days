# day 45
import requests
from mylib.cache import CacheFile
from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
cache_file = 'tmp/web.archive.org.empireonline.best-movies-2.html'

# avoid calls if needed
main_cache = CacheFile(cache_file)
if main_cache.is_cached():
    html = main_cache.get()
else:
    resp = requests.get(url)
    html = resp.text
    main_cache.save(html)

# clean things up for readability.. and save
soup = BeautifulSoup(html, 'html.parser')
cache_file = 'tmp/pretty.web.archive.org.empireonline.best-movies-2.html'
pretty_cache = CacheFile(cache_file)
if pretty_cache.is_cached():
    pretty_html = pretty_cache.get()
else:
    pretty_html = soup.prettify()
    pretty_cache.save(pretty_html)

#print(pretty_html)

soup = BeautifulSoup(pretty_html, 'html.parser')
print("Introducting the " + str(soup.title.getText()).strip())
print("ranked #1 to #100")

