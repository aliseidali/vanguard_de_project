#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!pip install spotipy --upgrade


# # Import spotify and extract data

# In[175]:


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd


# In[162]:


#Authentication - without user
cid='2037fdfce5ef42e690bea64a63f271df'
secret='bbe8c53af67342d3ad63e40ad5f72616'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


# In[193]:


## create artist info list
artist_info_list = ['spotify:artist:4S9EykWXhStSc15wEx8QFK','spotify:artist:4iHNK0tOyZPYnBU7nGAgpQ','spotify:artist:3DiDSECUqqY1AuBP8qtaIa','spotify:artist:5pKCCKE2ajJHZ9KAiaK11H',
 'spotify:artist:6XpaIBNiVzIetEPCWDvAFP','spotify:artist:6tbjWDEIzxoDsBA1FuhfPW','spotify:artist:3fMbdgg4jU18AjLCKBhRSm','spotify:artist:7guDJrEfX3qb6FEbdPA5qi',
 'spotify:artist:1zuJe6b1roixEKMOtyrEak','spotify:artist:66CXWjxzNUsdJxJ2JdwvnR','spotify:artist:1HY2Jd0NmPuamShAr6KMms','spotify:artist:0C8ZW7ezQVs4URX5aX7Kqx',
 'spotify:artist:6vWDO969PvNqNYHIOW5v0m','spotify:artist:2DlGxzQSjYe5N6G9nkYghR','spotify:artist:26dSoYclwsYLMAKD3tpOr4','spotify:artist:2NdeV5rLm47xAvogXrYhJX', 
 'spotify:artist:1yz6B7bGMEdZH4LlZx7odH','spotify:artist:7GaxyUddsPok8BuhxN6OUW','spotify:artist:23zg3TcAtWQy7J6upgbUnj','spotify:artist:2NdeV5rLm47xAvogXrYhJX']
len(artist_info_list)


# In[140]:


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


# In[141]:


# loop through each artist info and extract needed columns 
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


# In[210]:


artist_df = pd.DataFrame({'artist_id':artist_id,'artist_name':artist_name,'external_url':external_url,
                         'genre':genre,'image_url':image_url,'followers':followers,'popularity':popularity,'type':artist_type,
                         'artist_uri':artist_uri})
artist_df.head()


# In[253]:


# Create database and connection
import sqlite3
conn= sqlite3.connect('spotify.db')
c = conn.cursor()


# In[243]:


#Create artist table
c.execute('''CREATE TABLE IF NOT EXISTS artist (
                        artist_id  VARCHAR(50) PRIMARY KEY,
                        artist_name VARCHAR(255),
                        external_url VARCHAR(100),
                        genre VARCHAR(100),
                        image_url VARCHAR(100),
                        followers INT,
                        popularity INT,
                        type VARCHAR(50),
                        artist_uri VARCHAR(100)
                        );''')


# In[244]:


#Build and add the data to DataFrame
df = pd.DataFrame (artist_df, columns = ['artist_id','artist_name','external_url',
                         'genre','image_url','followers','popularity','type',
                         'artist_uri'])


# In[264]:


# Add data from DataFrame to sqlite
df.to_sql('artist', conn, if_exists='replace', index = False)


# In[245]:


c.execute('SELECT * FROM artist;')


# In[246]:


# Getting the data back from sqlite to DataFrame
df = pd.DataFrame(c.fetchall(), columns = ['artist_id','artist_name','external_url',
                        'genre','image_url','followers','popularity','type',
                        'artist_uri'])

print(df)


# In[247]:


# To check if table is created
c.execute("SELECT name from sqlite_master WHERE type = 'table';")
print(c.fetchall())


# In[240]:


# Function to retrieve album data from spotify api
def get_album_for_an_artist(artist_id,album_type='album',country='US'):
    album_list =[]
    album_id = []
    album_name = []
    external_url = []
    image_url = []
    release_date  =[]
    total_tracks =[]
    album_uri = []
    
    spotify = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    
    results = spotify.artist_albums(artist_id,album_type='album',country='US', limit = 20)
    albums = results['items']
    #print(results)
    while results['next']:
        results=spotify.next(results)
        albums.extend(results['items'])
    for album in albums:
        #print(album)
        if(album['name'] not in album_list):
            album_name.append(album['name'])
            album_id.append(album['id'])
            external_url.append(album['external_urls']['spotify'])
            image_url.append(album['images'][0]['url'])
            release_date.append(album['release_date'])
            total_tracks.append(album['total_tracks'])
            album_uri.append(album['uri'])
            #image_url.append(album['name'])
            #album_list.append(album['name'])
            #album_list.append(album['name'])
    
    df_album = pd.DataFrame({'album_name':album_name,'album_id':album_id,'external_url':external_url,
                            'image_url': image_url,'release_date':release_date,
                            'total_tracks':total_tracks,'album_uri':album_uri})  
            
    df_album['type'] = album_type
    df_album['artist_id'] = artist_id
      
    return df_album


# In[262]:


# Build the DataFrame 
df_album_all = pd.DataFrame()
for artist_info in artist_info_list:
    df_album = get_album_for_an_artist(artist_id=artist_info,album_type='album',country='US')
    df_album_all = pd.concat([df_album_all,df_album])
print(df_album_all.shape)
df_album_all.head()


# In[265]:


#Create album table
c.execute('''CREATE TABLE IF NOT EXISTS album (
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
                       REFERENCES artist(artist_id));''')


# In[257]:


# to check if album table is created
c.execute("SELECT name from sqlite_master WHERE type = 'table';")
print(c.fetchall())


# In[258]:


df = pd.DataFrame (df_album_all, columns = ['album_id','album_name','external_url',
                         'image_url','release_date','total_tracks','type','album_uri',
                         'artist_id'])


# In[227]:


df.to_sql('artist', conn, if_exists='replace', index = False)


# In[259]:


c.execute('SELECT * FROM artist')


# In[266]:


# To get back data sqlite to DataFrame
df = pd.DataFrame(c.fetchall(), columns = ['album_id','album_name','external_url','image_url',
                                       'release_date','total_tracks','type','album_uri','artist_id'])

print(df)


# In[ ]:




