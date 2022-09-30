
from db import *
from transformations import *
from visualizations import *
from APIcalls import *

#call functions for table creation and storing data
def store_data(conn, artist_data, album_data, tracks_data, track_features_data):
    pprint("==== Store Data into Database ==========")
    create_tables(conn)
    create_views(conn)           
    create_artist(conn, artist_data)
    create_album(conn, album_data)
    create_track(conn, tracks_data)
    create_track_feature(conn, track_features_data)

#Call view fuctions
def view_data(conn):
    pprint("===== View Data ================")
    pprint("===== Top 10 songs by artist in terms of duration_ms ================")
    view_top_songs_by_artist(conn)
    pprint("===== Top 20 artists in the database ordered by # of followers DESC ================")
    view_top_artists_by_followers(conn)
    pprint("===== Top 10 songs by artist in terms of tempo ================")
    view_top_songs_by_artist_tempo(conn)
    pprint("===== Top 10 songs by artist in terms of popularity ================")
    view_top_artists_by_popularity(conn)
    pprint("===== Top 10 songs by artist in terms of danceability ================")
    view_top_songs_by_artist_danceability(conn)

#Call visualizaton functions
def data_visualisation(conn):
    pprint("===== Data  visualisations =====")
    show_top_artists_by_followers(conn)
    show_top_artists_by_popularity(conn)
    show_most_played_artist(conn)


#Main method
def main():
    database = r"spotify.db"
    conn = create_connection(database)
    
    try:
        artist_data = get_artist_api()
        album_data = get_album_api()
        tracks_data = get_track_api(album_data)
        track_features_data = get_track_feature_api(tracks_data)
        with conn:
            store_data(conn, artist_data, album_data, tracks_data, track_features_data)
            view_data(conn)    
            data_visualisation(conn)            

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
if __name__ == '__main__':
    main()