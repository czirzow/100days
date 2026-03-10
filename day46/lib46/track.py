
from dataclasses import dataclass

@dataclass
class Track:
    id: str
    name: str
    artist: str

    artist_id: str = ""
    album_id: str = ""

if True:
    t = Track(id='ff930', 
              name='Track Name', 
              artist='Artist Name')
    print(t)

