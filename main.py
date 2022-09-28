
from db import *
from webAPIs import *

def main():
    database = r"C:\Users\alise\OneDrive\Desktop\Onramp_project\db\spotipy.db"
    conn = create_connection(database)
    artist_data = getArtistAPI()
    try:
        with conn:
            create_tables(conn)
            create_artist(conn, artist_data)
            #create_album(conn, album_data)
            #create_track(conn, track_data)
            #create_track_feature(conn, track_feature_data)

            view_artist(conn)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
if __name__ == '__main__':
    main()