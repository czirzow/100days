# day 45
from hashlib import md5
import requests
from mylib.cache import CacheFile
from bs4 import BeautifulSoup
from pprint import pprint


TMP_DIR = 'tmp/'


url = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

### Test code on how to figure out a good cache_file name
if True:
    from urllib.parse import urlparse
    import hashlib
    def get_cache_file(url:str, name:str, type:str='json'):
        ## this is the __init__() for Cache?
        tmp_dir:str = TMP_DIR
        #try:
        u = urlparse(url)
        #pprint(u)
        f = f"{tmp_dir}{u.netloc}.{name}"

        hashkey:str = f + u.query + u.params
        #try:
        hash = hashlib.sha256(hashkey.encode()).hexdigest()[:8]
        f += f".{hash}.{type}"

        #print("F is:", f)
        return f


cache_file = get_cache_file(url=url, name='best-movies-2', type='html')

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
titles = soup.select(selector='div .entity-info-items__list ul li a')
ranked = [ t.getText().strip() for t in titles ][::-1]
#ranked.reverse()
pprint(ranked)







