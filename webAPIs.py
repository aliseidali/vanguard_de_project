import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='2037fdfce5ef42e690bea64a63f271df', client_secret = 'bbe8c53af67342d3ad63e40ad5f72616'))

def getArtistId():
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
                        "artist_id" : "6tbjWDEIzxoDsBA1FuhfPW",
                        "artist_name" : "Madonna"
                    },
                    {
                        "artist_id" : "3fMbdgg4jU18AjLCKBhRSm",
                        "artist_name" : "Michael Jackson"
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
                        "artist_id" : "3FhFPU1KZfHV3sbQSYAmI4",
                        "artist_name" : "Christopher Brown"
                    },
                    {
                        "artist_id" : "7GaxyUddsPok8BuhxN6OUW",
                        "artist_name" : "James Brown"
                    },
                    {
                        "artist_id" : "23zg3TcAtWQy7J6upgbUnj",
                        "artist_name" : "Usher"
                    }
                ]
    return artist_ids

def getArtistAPI():
    artist_data = []
    artist_ids = getArtistId()

    for id in artist_ids:
        urn = 'spotify:artist:' + id['artist_id']
        artist = sp.artist(urn)
        name = artist['name']
        id = artist['id']
        external_urls = artist["external_urls"]["spotify"]
        followers = artist["followers"]["total"]
        popularity = artist["popularity"]
        artist_type = artist["type"]
        artist_uri = artist["uri"]
        genres = artist['genres']
        genre = ""
       
        if len(genres) > 0:
            genre = artist['genres'][0]

        images = artist['images']
        image_url = ""
        if len(images) > 0:
            image_url = artist['images'][0]['url']            

        data = (id, name, external_urls, genre, image_url, followers, popularity, artist_type, artist_uri)
       
        artist_data.append(data)
 
    return artist_data