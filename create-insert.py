import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_tables(conn, sql):
    
    cur = conn.cursor()
    cur.execute(sql)
   
    return conn

def create_artist(conn, artist_data):
    sql = '''INSERT INTO artist(artist_id,artist_name,external_url)
              VALUES(?,?,?) '''
    cur = conn.cursor()

    cur.executemany(sql,artist_data)

    return cur.lastrowid

def view_artist(conn):
    cur = conn.cursor()
   
    for row in cur.execute("SELECT * FROM artist"):
        print(row)

    return cur

def get_artist():
     
    artist_data = [
            ("1", "Teddy Afro", "www.google.com"),
            ("2", "Mohammod Ahmed", "www.google.com"),
            ("3", "Aster Awake", "www.google.com")]
    
    return artist_data





def main():
    print("========= App Staring ======================")
    database =  r"C:\Users\alise\OneDrive\Desktop\Onramp_project\db\spotipy.db"

    artist_table_sql = ''' CREATE TABLE IF NOT EXISTS artist (
                        artist_id  VARCHAR (50) PRIMARY KEY,
                        artist_name VARCHAR (255),
                        external_url VARCHAR (255),
                        genre VARCHAR (255),
                        image_url VARCHAR (255),
                        followers INT);'''

    conn = create_connection(database)
    create_tables(conn, artist_table_sql)
    
    artist_data = get_artist()
    create_artist(conn, artist_data)
    view_artist(conn)
    print("========= DONE ======================")

if __name__ == '__main__':
    main()