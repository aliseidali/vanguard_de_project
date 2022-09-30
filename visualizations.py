from db import *
from APIcalls import *
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint


#Create visualizations
def show_top_artists_by_followers(conn):
    artists = view_top_artists_by_followers(conn)    
    pprint(artists)

    artist_names = []
    artist_followers = []
    for artist in artists:
            artist_names.append(artist["Artist Name"])  
            artist_followers.append(artist["Followers"])
    x = np.array(artist_names)
    y = np.array(artist_followers)
    plt.title("Artists with Followers")
    plt.xlabel("Artist Name")
    plt.ylabel("Followers")
    plt.xticks(fontsize=6, rotation=90)
    plt.bar(x, y, width = 0.5)
    plt.show()

def show_top_artists_by_popularity(conn):
    artists = view_top_artists_by_popularity(conn)    
    artist_names = []
    artist_popularity = []
    for artist in artists:
            artist_names.append(artist["Artist Name"])  
            artist_popularity.append(artist["Popularity"])

    x = np.array(artist_names)
    y = np.array(artist_popularity)
    plt.title("Artists with Popularity")
    plt.xlabel("Artist Name")
    plt.ylabel("Popularity")
    plt.xticks(fontsize=6, rotation=90)
    plt.bar(x, y, width = 0.5)
    plt.show()      

def show_most_played_artist(conn):
    artists = view_top_songs_by_artist(conn)    
    artist_names = []
    artist_duration = []
    for artist in artists:
            artist_names.append(artist["Artist Name"])  
            artist_duration.append(artist["Duration"] * 6000)

    x = np.array(artist_names)
    y = np.array(artist_duration)
    plt.title("Most Played Artist")
    plt.xlabel("Artist Name")
    plt.ylabel("Minutes Played")
    plt.xticks(fontsize=6, rotation=90)
    plt.bar(x, y, width = 0.5)
    plt.show()    



