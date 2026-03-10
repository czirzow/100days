import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
from pprint import pprint

from lib46.cache_file import cache_file
from mylib.cache import CacheJson

load_dotenv()


CLIENT_ID = os.environ['SPOTIPY_CLIENT_ID']
CLIENT_SECRET = os.environ['SPOTIPY_CLIENT_SECRET']
REDIRECT_URI = "https://example.com/"
scope = "playlist-modify-private,playlist-read-private"


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
        scope=scope,
        cache_path="data/spotify-token.txt"))

#user_id = sp.current_user()["id"]
#print(user_id)

# DEBUG: oath is not working.
if False:
    # basic usage that should work.
    playlists = sp.current_user_playlists()
    pprint(playlists)
    exit()


# SPOTIFY is down... so lets comment...
# and the  rest continues

#drews_music_id = '6hJXWUx16oeGzKp4BkuocY'
#dews_music = sp.playlist(drews_music_id)

# this is the actual api call.
from functools import partial
guitar_songs_id = '2z6LRqzNYbzxOVFdGidDoi'

url = f"https://api.spotify.com/v1/playlists/{guitar_songs_id}/items"
file = cache_file(url, 'my.guitar.songs')

# setup the call back in the case that we don't have a cache file.
get_guitar_songs = partial(sp.playlist, guitar_songs_id)
cache = CacheJson(file, callback=get_guitar_songs)


if False:
    # DEBUG: lets make sure the api call works.
    cache.clear()

exit(1)

guitar_songs = cache.get()
pprint(guitar_songs)
print(type(guitar_songs))
# expect the json file results.

exit()

if cache.is_cached():
    print("Cached!!")
    guitar_songs = cache.get()
else:
    guitar_songs = sp.playlist(guitar_songs_id)
    cache.save(guitar_songs)

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



