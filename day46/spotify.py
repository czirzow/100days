import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from lib46.cache_file import cache_file
from mylib.cache import CacheJson

from dotenv import load_dotenv
load_dotenv()
CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']

# 
REDIRECT_URI = "http://localhost/"
SPTY_SCOPE = "playlist-modify-private,playlist-read-private"


# A thought: since we will be caching results
#            lets create a way to authenticate on demand.
#  class MyOAuth():
#      def __init__(self):
#          pass
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SPTY_SCOPE,
        cache_path="data/spotify-token.txt"))


from pprint import pprint
#DEBUG: step back a bit.
if False:
    """if things are not working propery"""
    user_id = sp.current_user()["id"]
    print(user_id)
    exit()

# DEBUG: oath is not working.
if False:
    # basic usage that should work.
    playlists = sp.current_user_playlists()
    pprint(playlists)
    exit()


from functools import partial


# setup the call back in the case that we don't have a cache file.
"""The playlist id"""
guitar_songs_id = '2z6LRqzNYbzxOVFdGidDoi'

"""The fields to return from the api call"""
fields = ['items.item.name',
          'items.item.id',
          'items.item.artists.name',
          'items.item.artists.id',
          'offset',
          'total',
          ]

# configure a callback for the cache if we need to renew data.
get_guitar_songs = partial(sp.playlist_items, 
                           guitar_songs_id, 
                           fields=','.join(fields))

# TODO: be able to render this url from the spotipy requests.url
# for the time being we fake it and change names as needed. 
# to cache requests.
url = f"https://api.spotify.com/v1/playlists/{guitar_songs_id}/items"
file = cache_file(url, 'my.guitar.songs2')

#print(get_guitar_songs())
cache = CacheJson(file, callback=get_guitar_songs)

if False:
    # DEBUG: lets make sure the api call works.
    cache.clear()


guitar_songs = cache.get()
exit()
#pprint(guitar_songs)
#print(type(guitar_songs))
# expect the json file results.


print(guitar_songs['items']['total'])

for song_details in guitar_songs['items']['items']:
    song = song_details['item']
    print(song['name'], song['uri'])
    album = song['album']
    print(" "*2, album['name'], album['uri'])
    for artist in song['artists']:
        print(" "*4, artist['name'], artist['uri'])




# TODO:
# get playlist
# save play liist info to file.


# create sublists:
#   ska like
#   punk like
#   [genre like items]
# save into a file  in a spotiy format.


# read saved list
# put save list to spotify



