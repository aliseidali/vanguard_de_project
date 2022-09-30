import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
from pprint import pprint
from transformations import *


### Insert the Client_ID and Client_ Secret

CLIENT_ID = '??????????'
CLIENT_SECRET = '?????????????'

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret = CLIENT_SECRET))

#def get_artist_ids():

artist_ids = [
                    {
                        "artist_id" : "4S9EykWXhStSc15wEx8QFK",
                        "artist_name" : "Celine Dion"
                    },
                    {
                        "artist_id" : "4iHNK0tOyZPYnBU7nGAgpQ",
                        "artist_name" : "Mariah Carey"
                    },
                    {
                        "artist_id" : "3DiDSECUqqY1AuBP8qtaIa",
                        "artist_name" : "Alicia Keys"
                    },
                    {
                        "artist_id" : "5pKCCKE2ajJHZ9KAiaK11H",
                        "artist_name" : "Rihanna"
                    },
                    {
                        "artist_id" : "6XpaIBNiVzIetEPCWDvAFP",
                        "artist_name" : "Whitney Houston"
                    },
                    {
                        "artist_id" : "6tbjWDEIzxoDsBA1FuhfPW",
                        "artist_name" : "Madonna"
                    },
                    {
                        "artist_id" : "3fMbdgg4jU18AjLCKBhRSm",
                        "artist_name" : "Michael Jackson"
                    },
                    {
                        "artist_id" : "7guDJrEfX3qb6FEbdPA5qi",
                        "artist_name" : "Stevie Wonder"
                    },
                    {
                        "artist_id" : "1zuJe6b1roixEKMOtyrEak",
                        "artist_name" : "Tina Turner"
                    },
                    
                    {
                        "artist_id" : "66CXWjxzNUsdJxJ2JdwvnR",
                        "artist_name" : "Ariana Grande"
                    },
                    {
                        "artist_id" : "1HY2Jd0NmPuamShAr6KMms",
                        "artist_name" : "Lady Gaga"
                    },
                    {
                        "artist_id" : "0C8ZW7ezQVs4URX5aX7Kqx",
                        "artist_name" : "Selena Gomez"
                    },
                    {
                        "artist_id" : "6vWDO969PvNqNYHIOW5v0m",
                        "artist_name" : "Beyonce Knowles"
                    },
                    {
                        "artist_id" : "2DlGxzQSjYe5N6G9nkYghR",
                        "artist_name" : "Jennifer Lopez"
                    },
                    {
                        "artist_id" : "26dSoYclwsYLMAKD3tpOr4",
                        "artist_name" : "Britney Spears"
                    },
                    {
                        "artist_id" : "4qwGe91Bz9K2T8jXTZ815W",
                        "artist_name" : "Janet Jackson"
                    },
                    {
                        "artist_id" : "0hCNtLu0JehylgoiP8L4Gh",
                        "artist_name" : "Nicki Minaj"
                    },
                    {
                        "artist_id" : "7GaxyUddsPok8BuhxN6OUW",
                        "artist_name" : "James Brown"
                    },
                    {
                        "artist_id" : "23zg3TcAtWQy7J6upgbUnj",
                        "artist_name" : "Usher"
                    },
                    {
                        "artist_id" : "2NdeV5rLm47xAvogXrYhJX",
                        "artist_name" : "Ciara"
                    }
                ]



    #return artist_ids
    
#api call for artist data
def get_artist_api():
    artist_data = []
    #artist_ids = get_artist_ids()
    pprint("======================================== Loading Artists===============================")
    for id in artist_ids:
        urn = 'spotify:artist:' + id['artist_id']
        artist = sp.artist(urn)        
        this_data = map_artist(artist)
        artist_data.append(this_data)
    return artist_data

#api call for album data
def get_album_api():
    album_data = []
    #artist_ids = get_artist_ids()    
    pprint("==== Loading Albums =====")

    for id in artist_ids:
        artist_uri = 'spotify:artist:' + id['artist_id']
        results = sp.artist_albums(artist_uri, album_type='album')
        albums = results['items']
        while results['next']:
            results = sp.next(results)
            albums.extend(results['items'])
        for album in albums:
            this_album = map_album(album, id['artist_id'])
            album_data.append(this_album)
    return album_data

#api call for track data
def get_track_api(album_data):
    track_data = [] 
    pprint("==== Loading Tracks ====")

    for album in album_data:
        album_id = album["album_id"]
        track_uri = 'spotify:album:' + album_id
        results = sp.album_tracks(track_uri)
        track_results = results["items"]
        for song in track_results:           
            track_feature_uri = 'spotify:track:' + song["id"]
           
            track_feature = []           
            this_track = map_track(song, album_id)
            track_data.append(this_track)
    
    return track_data

#api call for track feature data
def get_track_feature_api(track_data):
    track_feature_data = []
    print("======== Loading Track Features ====")
    track_ids = []
    
    for track in track_data:
        track_ids.append(track["track_id"])
    
    itemOffset = 0
    itemsPerPage = 10
    endOffset = itemOffset + itemsPerPage
    
    for track in track_data:        
        #track_feature_data.extend(track['features'])   
        track_feature_uri = track["track_id"]
        features = sp.audio_features(track_feature_uri)
        track_feature = []            
        for feature in features:
            this_feature = map_track_feature(feature)
            track_feature_data.append(this_feature)
    return track_feature_data