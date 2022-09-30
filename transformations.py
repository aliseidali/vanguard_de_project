from pprint import pprint
import datetime

#Mapping for artist table
def map_artist(artist_json):     
    genres = artist_json['genres']
    genre = ""
       
    if len(genres) > 0:
        genre = artist_json['genres'][0]

    images = artist_json['images']
    image_url = ""
    if len(images) > 0:
        image_url = artist_json['images'][0]['url'] 

    this_artist = {
        "artist_id" : artist_json['id'],
        "artist_name" : artist_json['name'],
        "external_url" : artist_json["external_urls"]["spotify"],
        "genre" : genre,
        "image_url" : image_url,
        "followers" : artist_json["followers"]["total"],
        "popularity" : artist_json["popularity"],
        "type" : artist_json["type"],
        "artist_uri" : artist_json["uri"]
    }


    return this_artist

#Mapping for album table
def map_album(album, artist_id):
    album_id = album["id"]
    album_name = album["name"]
    external_url = album["external_urls"]["spotify"]
    release_date = album["release_date"]
    total_tracks = album["total_tracks"]
    album_type = album["album_type"]
    album_uri = album["uri"]
    images = album['images']
    image_url = ""
    if len(images) > 0:
        image_url = album['images'][0]['url']  

    this_album = {
        "album_id" : album_id,
        "album_name" : album_name,
        "external_url" : external_url,
        "image_url" : image_url,
        "release_date" : release_date,
        "total_tracks" : total_tracks,
        "album_type" : album_type,
        "album_uri" : album_uri,
        "artist_id" : artist_id
    }
    
    return this_album

#Mapping for track table
def map_track(track, album_id):
   
    disc_number = track["disc_number"]
    duration_ms = track["duration_ms"]
    track_id = track["id"]
    external_url = track["external_urls"]["spotify"]
    song_name = track["name"]
    explicit = track["explicit"]
    song_uri = track["uri"]
    track_type = track["type"]

    this_data = {
        "track_id" : track_id,
        "song_name" : song_name,
        "external_url" : external_url,
        "duration_ms" : duration_ms,
        "explicit" : explicit,
        "disc_number" : disc_number,
        "type" : track_type,
        "song_uri" : song_uri,
        "album_id" : album_id
    }

    return this_data

#Mapping for track feature table
def map_track_feature(track_feature):   
   
    track_id = track_feature["id"]
    danceability = track_feature["danceability"]
    energy = track_feature["energy"]
    instrumentalness = track_feature["instrumentalness"]
    liveness = track_feature["liveness"]
    loudness = track_feature["loudness"]
    speechiness = track_feature["speechiness"]
    tempo = track_feature["tempo"]
    feature_type = track_feature["type"]
    valence = track_feature["valence"]
    uri = track_feature["uri"]  
    data = {
        "track_id" : track_id, "danceability" : danceability, 
        "energy" : energy, "instrumentalness" : instrumentalness, 
        "liveness": liveness, "loudness" : loudness, 
        "speechiness" : speechiness, "tempo" : tempo, 
        "type" : feature_type, "valence" : valence, "song_uri" : uri
    }

    return data

   
   