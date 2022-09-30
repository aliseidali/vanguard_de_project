import sqlite3
from sqlite3 import Error
from pprint import pprint
import datetime
import pandas as pd

#create database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

#create the four tables
def create_tables(conn):    
    cur = conn.cursor()
    sqls = [''' CREATE TABLE IF NOT EXISTS Artist (
                        artist_id  VARCHAR (50),
                        artist_name VARCHAR (255),
                        external_url VARCHAR (100),
                        genre VARCHAR (100),
                        image_url VARCHAR (100),
                        followers INT,
                        popularity INT,
                        type VARCHAR (50),
                        artist_uri VARCHAR (100))''', 
                    '''CREATE TABLE IF NOT EXISTS Album (
                        album_id  VARCHAR (50),
                        album_name VARCHAR (255),
                        external_url VARCHAR (100),
                        image_url VARCHAR (100),
                        release_date DATE,
                        total_tracks INT,
                        type VARCHAR (50),
                        album_uri VARCHAR (255),
                        artist_id VARCHAR (50))''' , 
                    '''CREATE TABLE IF NOT EXISTS Track (
                        track_id  VARCHAR (50),
                        song_name VARCHAR (255),
                        external_url VARCHAR (100),
                        duration_ms INT,
                        explicit BOOLEAN,
                        disc_number	 INT,
                        type VARCHAR (50),
                        song_uri VARCHAR (255),
                        album_id VARCHAR (50))''',
                    '''CREATE TABLE IF NOT EXISTS track_feature (
                        track_id  VARCHAR (50),
                        danceability DOUBLE,
                        energy DOUBLE,
                        instrumentalness DOUBLE,
                        liveness DOUBLE,
                        loudness DOUBLE,
                        speechiness DOUBLE,
                        tempo DOUBLE,                     
                        type VARCHAR (50),
                        valence DOUBLE,
                        song_uri VARCHAR (100))''']
    for sql in sqls:
        cur.execute(sql)
    return conn

#create views
def create_views(conn):
    cur = conn.cursor()
    sqls = ['''DROP VIEW IF EXISTS  top_songs_by_artist ''', 
            ''' CREATE VIEW IF NOT EXISTS  top_songs_by_artist 
                    AS 
                        SELECT
                            DISTINCT 
                            artist.artist_name as 'Artist Name',                                                      
                            album.album_name as 'Album Name',
                            track.song_name as 'Song Name',                           
                            track.duration_ms as 'Duration'
                        FROM  track
                        INNER JOIN album ON track.album_id = album.album_id 
                        INNER JOIN artist ON album.artist_id = artist.artist_id 
                        GROUP BY album.album_id
                        ORDER BY artist.artist_name asc, duration_ms DESC 
                        LIMIT 20
                ''',
                
                '''DROP VIEW IF EXISTS  top_artists_by_followers ''', 
                ''' CREATE VIEW IF NOT EXISTS  top_artists_by_followers 
                    AS 
                        SELECT 
                            DISTINCT                                              
                            artist_name as 'Artist Name',
                            followers  as 'Followers'                        
                        FROM artist
                        ORDER BY followers DESC 
                        LIMIT 20
                ''',
                '''DROP VIEW IF EXISTS  top_songs_by_artist_tempo''', 
                '''CREATE VIEW IF NOT EXISTS  top_songs_by_artist_tempo 
                    AS 
                        SELECT
                            DISTINCT
                            artist.artist_name as 'Artist Name',
                            album.album_name as 'Album Name',
                            track.song_name as 'Song Name',                            
                            track_feature.tempo as 'Tempo'
                        FROM  artist
                        INNER JOIN album ON artist.artist_id = album.artist_id 
                        INNER JOIN track ON album.album_id = track.album_id
                        INNER JOIN track_feature ON track.track_id = track_feature.track_id                    
                        GROUP BY album.album_id
                        ORDER BY track_feature.tempo DESC  
                        LIMIT 10                    
                ''',
                '''DROP VIEW IF EXISTS  top_artists_by_popularity ''', 
                ''' CREATE VIEW IF NOT EXISTS  top_artists_by_popularity 
                    AS 
                        SELECT 
                            DISTINCT                                              
                            artist_name as 'Artist Name',
                            popularity as 'Popularity'                         
                        FROM artist
                        ORDER BY popularity DESC 
                        LIMIT 20
                ''',
                 '''DROP VIEW IF EXISTS  top_songs_by_artist_danceability''', 
                '''CREATE VIEW IF NOT EXISTS  top_songs_by_artist_danceability 
                    AS 
                        SELECT
                            DISTINCT
                            artist.artist_name as 'Artist Name',
                            album.album_name as 'Album Name',
                            track.song_name as 'Song Name',                           
                            track_feature.danceability as 'Danceablity'
                        FROM  artist
                        INNER JOIN album ON artist.artist_id = album.artist_id 
                        INNER JOIN track ON album.album_id = track.album_id
                        INNER JOIN track_feature ON track.track_id = track_feature.track_id                    
                        GROUP BY album.album_id
                        ORDER BY track_feature.danceability DESC  
                        LIMIT 10                    
                '''
                ]

    for sql in sqls:
        cur.execute(sql)
    return conn

#Insert data into tables
def insert_into_table(conn, sql, data):
    cur = conn.cursor()
    cur.executemany(sql, data)
    return cur.lastrowid

#Insert data into artist table
def create_artist(conn, dict_data):
    
    artists_data = []
    sql = '''INSERT INTO Artist(artist_id,artist_name,external_url, genre, image_url, followers, popularity, type, artist_uri)
              VALUES(?,?,?,?,?,?,?,?,?) '''
    for this_value in dict_data:
        this_data = list((this_value["artist_id"], this_value["artist_name"], this_value["external_url"], this_value["genre"],
                     this_value["image_url"],this_value["followers"], this_value["popularity"], this_value["type"], this_value["artist_uri"]))
        artists_data.append(this_data)
    
    return insert_into_table(conn, sql, artists_data)

#Insert into album table
def create_album(conn, dict_data):
    album_data = []
    sql = '''INSERT INTO Album(album_id, album_name, external_url, image_url, release_date, total_tracks, type, album_uri, artist_id)
              VALUES(?,?,?,?,?,?,?,?,?) ''' 
     
    for this_value in dict_data:
        this_data = list((this_value["album_id"], this_value["album_name"], this_value["external_url"], this_value["image_url"],
                     this_value["release_date"],this_value["total_tracks"], this_value["album_type"], this_value["album_uri"], this_value["artist_id"]))
        album_data.append(this_data)
    
    return insert_into_table(conn, sql, album_data)

#Insert into track table   
def create_track(conn, dict_data):
    track_data = []
    sql = '''INSERT INTO Track(
                        track_id,
                        song_name,
                        external_url,
                        duration_ms,
                        explicit,
                        disc_number,
                        type,
                        song_uri,
                        album_id
                        ) VALUES(?,?,?,?,?,?,?,?,?)'''

    for this_value in dict_data:
        this_data = list((this_value["track_id"], this_value["song_name"], this_value["external_url"], this_value["duration_ms"],
                     this_value["explicit"],this_value["disc_number"], this_value["type"], this_value["song_uri"], 
                     this_value["album_id"]))
        track_data.append(this_data)

    return insert_into_table(conn, sql, track_data)
    
#Insert into track feature table
def create_track_feature(conn, dict_data):
    track_feature_data = []
    sql = '''INSERT INTO Track_Feature(
                        track_id,
                        danceability,
                        energy,
                        instrumentalness,
                        liveness,
                        loudness,
                        speechiness,
                        tempo,                     
                        type,
                        valence,
                        song_uri) VALUES(?,?,?,?,?,?,?,?,?,?,?)''' 
    
    for this_value in dict_data:
        this_data = list((this_value["track_id"], this_value["danceability"], this_value["energy"], this_value["instrumentalness"],
                     this_value["liveness"],this_value["loudness"], this_value["speechiness"], this_value["tempo"], 
                     this_value["type"],  this_value["valence"],  this_value["song_uri"]))
        track_feature_data.append(this_data)

    return insert_into_table(conn, sql, track_feature_data)   

#creating views
def view_data(conn, sql):
    cur = conn.cursor() 
    columns = []
    rows = []
    dict_data = []

    sql_data = cur.execute(sql)
    for column in sql_data.description:
        columns.append(column[0])
        
    for row in sql_data:  
        this_value = {           
        }      
        for i in range(len(columns)):
            this_value.update({
               columns[i] : row[i] 
            })
        
        dict_data.append(this_value)
            
   
  
    return dict_data

def view_artist(conn):
    sql = "SELECT * FROM Artist"       
    return view_data(conn, sql)

def view_album(conn):
    sql = "SELECT * FROM Album"       
    return view_data(conn, sql)

def view_track(conn):
    sql = "SELECT * FROM Track"       
    return view_data(conn, sql)

def view_track_feature(conn):
    sql = "SELECT * FROM Track_Feature"       
    return view_data(conn, sql)

def view_top_songs_by_artist(conn):
    sql = "SELECT * FROM top_songs_by_artist"       
    dict_data = view_data(conn, sql)
    df_data = pd.DataFrame(dict_data)
    pprint(df_data)
    return dict_data

def view_top_artists_by_followers(conn):
    sql = "SELECT * FROM top_artists_by_followers"       
    dict_data = view_data(conn, sql)
    df_data = pd.DataFrame(dict_data)
    pprint(df_data)
    return dict_data

def view_top_songs_by_artist_tempo(conn):
    sql = "SELECT * FROM top_songs_by_artist_tempo"  
    dict_data = view_data(conn, sql)
    df_data = pd.DataFrame(dict_data)
    pprint(df_data)
    return dict_data

def view_top_artists_by_popularity(conn):
    sql = "SELECT * FROM top_artists_by_popularity"  
    dict_data = view_data(conn, sql)
    df_data = pd.DataFrame(dict_data)
    pprint(df_data)
    return dict_data

def view_top_songs_by_artist_danceability(conn):
    sql = "SELECT * FROM top_songs_by_artist_danceability"  
    dict_data = view_data(conn, sql)
    df_data = pd.DataFrame(dict_data)
    pprint(df_data)
    return dict_data


  

    
    

