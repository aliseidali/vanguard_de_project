import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys


uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='b88548c7546a4e6a99b512ba0e8d29db', client_secret = '8a114d78cc764d3da2a96f64c0a0a0b7'))

results = sp.artist_albums(uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album["name"])