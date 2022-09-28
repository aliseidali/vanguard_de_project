import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def create_tables(conn):    
    cur = conn.cursor()
    sqls = [''' CREATE TABLE IF NOT EXISTS artist (
                        artist_id  VARCHAR(50) PRIMARY KEY,
                        artist_name VARCHAR(255),
                        external_url VARCHAR(100),
                        genre VARCHAR(100),
                        image_url VARCHAR(100),
                        followers INT,
                        popularity INT,
                        type VARCHAR(50),
                        artist_uri VARCHAR(100)
                        );''',

            '''CREATE TABLE IF NOT EXISTS album (
                        album_id  VARCHAR(50) PRIMARY KEY,
                        album_name VARCHAR(255),
                        external_url VARCHAR(100),
                        image_url VARCHAR(100),
                        release_date date,
                        total_tracks INT,
                        type VARCHAR(50),
                        album_uri VARCHAR(100),
                        artist_id VARCHAR(50),
                        CONSTRAINT fk_artist FOREIGN KEY(artist_id) 
                        REFERENCES artist(artist_id));''',
            '''CREATE TABLE IF NOT EXISTS track (
                        track_id  VARCHAR(50) PRIMARY KEY,
                        song_name VARCHAR(255),
                        external_url VARCHAR(100),
                        duration_ms	INT,
                        explicit boolean,
                        disc_number INT,
                        type VARCHAR(50),
                        song_uri VARCHAR(100),
                        album_id VARCHAR(50)
                        );''',
            '''CREATE TABLE IF NOT EXISTS track_feature(
                        track_id  VARCHAR(50) PRIMARY KEY,
                        danceability double,
                        energy double,
                        instrumentalness double,
                        liveness double, 
                        loudness double,
                        speechiness double,
                        tempo double,
                        type VARCHAR(50),
                        valence double,
                        song_uri VARCHAR(100));'''            
                        
                  
        ]
    for sql in sqls:
        cur.execute(sql)
    return conn

def insert_into_table(conn, sql, data):
    cur = conn.cursor()
    cur.executemany(sql, data)
    return cur.lastrowid

def create_artist(conn, data):
    sql = '''INSERT INTO artist(artist_id,artist_name,external_url, genre, image_url, followers, popularity,type, artist_uri)
              VALUES(?,?,?,?,?,?,?,?,?) '''  
    return insert_into_table(conn, sql, data)

def create_album(conn, data):
    sql = '''INSERT INTO album(album_id, album_name, external_url, image_url, release_date, total_trucks, type, album_uri, artist_id)
              VALUES(?,?,?,?,?,?,?,?,?) '''
    return insert_into_table(conn, sql, data)

def create_track(conn, data):
    sql = '''INSERT INTO track(track_id, song_name, external_url, duration_ms, explicit, disc_number, type, song_uri,album_id)
              VALUES(?,?,?,?,?,?,?,?,?) '''
    return insert_into_table(conn, sql, data)

def create_track_feature(conn, data):
    sql = '''INSERT INTO track_feature(track_id, Danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, type, valence,song_uri)
              VALUES(?,?,?,?,?,?,?,?,?,?,?) '''    
    return insert_into_table(conn, sql, data)   

def view_data(conn, sql):
    cur = conn.cursor()   
    for row in cur.execute(sql):
        print(row)
    return cur

def view_artist(conn):
    sql = "SELECT * FROM artist"       
    return view_data(conn, sql)
#added code



    