import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='2037fdfce5ef42e690bea64a63f271df', client_secret = 'bbe8c53af67342d3ad63e40ad5f72616'))

urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
sp = spotipy.Spotify()

artist = sp.artist(urn)
print(artist)

#user = sp.user('plamere')
#print(user)