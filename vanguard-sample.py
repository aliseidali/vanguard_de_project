import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import pprint


spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='2037fdfce5ef42e690bea64a63f271df', client_secret = 'bbe8c53af67342d3ad63e40ad5f72616'))
name = "foo fighters"

results = spotify.search(q='artist:' + name, type='artist')
items = results['artists']['items']
artist_uri = ""
if len(items) > 0:
    artist = items[0]
    pprint.pprint(artist)
    artist_uri = artist["uri"]
    # print(artist['name'], artist['images'][0]['url'])

results = spotify.artist_albums(artist_id = artist_uri, album_type = 'album', country = 'US')
# pprint.pprint(results['items'][0])
album_id = results['items'][0]['id']

results = spotify.album_tracks(album_id = album_id, limit=50, offset=0)
# pprint.pprint(results['items'][0])
track_id = results['items'][0]['id']

results = spotify.audio_features([track_id])
pprint.pprint(results)