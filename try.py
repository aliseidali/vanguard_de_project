import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd


sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='2037fdfce5ef42e690bea64a63f271df', client_secret = 'bbe8c53af67342d3ad63e40ad5f72616'))

## create artis info list
artist_info_list = ['spotify:artist:4S9EykWXhStSc15wEx8QFK','spotify:artist:4iHNK0tOyZPYnBU7nGAgpQ','spotify:artist:3DiDSECUqqY1AuBP8qtaIa','spotify:artist:5pKCCKE2ajJHZ9KAiaK11H',
 'spotify:artist:6XpaIBNiVzIetEPCWDvAFP','spotify:artist:6tbjWDEIzxoDsBA1FuhfPW','spotify:artist:3fMbdgg4jU18AjLCKBhRSm','spotify:artist:7guDJrEfX3qb6FEbdPA5qi',
 'spotify:artist:1zuJe6b1roixEKMOtyrEak','spotify:artist:66CXWjxzNUsdJxJ2JdwvnR','spotify:artist:1HY2Jd0NmPuamShAr6KMms','spotify:artist:0C8ZW7ezQVs4URX5aX7Kqx',
 'spotify:artist:6vWDO969PvNqNYHIOW5v0m','spotify:artist:2DlGxzQSjYe5N6G9nkYghR','spotify:artist:26dSoYclwsYLMAKD3tpOr4','spotify:artist:2NdeV5rLm47xAvogXrYhJX', 
 'spotify:artist:3FhFPU1KZfHV3sbQSYAmI4','spotify:artist:7GaxyUddsPok8BuhxN6OUW','spotify:artist:23zg3TcAtWQy7J6upgbUnj','spotify:artist:2NdeV5rLm47xAvogXrYhJX']
len(artist_info_list)



## create empty list to store data for each attributes of an artist
artist_id = []
artist_name = []
external_url=[]
genre=[]
image_url=[]
followers=[]
popularity =[]
artist_type =[]
artist_uri =[]


for artist_info in artist_info_list:
    artist = sp.artist(artist_info)
    artist_id.append(artist['id'])
    artist_name.append(artist['name'])
    external_url.append(artist['external_urls']['spotify'])
    #genre.append(artist['genres'][0])
    genre += [artist['genres'][0]] if len(artist['genres'])>0  else [""]
    image_url.append(artist['images'][0]['url'])
    followers.append(artist[ 'followers']['total'])
    popularity.append(artist['popularity'])
    artist_type.append(artist['type'])
    artist_uri.append(artist['uri'])

artist_df = pd.DataFrame({'artist_id':artist_id,'artist_name':artist_name,'external_url':external_url,
                         'genre':genre,'image_url':image_url,'followers':followers,'popularity':popularity,'type':artist_type,
                         'artist_uri':artist_uri})
artist_df.head()