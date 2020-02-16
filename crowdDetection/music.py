import sys
import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials


def show_tracks(results):
    tracklist = []
    lol = min(5,len(results['items']))
    for i in range(0,lol):
        j = random.randint(0,len(results['items']) - 1)
        track = results['items'][j]['track']
        l = track['artists'][0]['name']
        m = track['name']
        n = track['album']['images'][0]['url']
        artist = {'name': l, 'song': m, 'url': n}
        tracklist.append(artist)
    return tracklist

def get_songs(emotion):
    client_credentials_manager = SpotifyClientCredentials('API_KEY','SECRET_KEY')
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    user = 'shriram.holla'
    song_name = 'Random'
    playlists = sp.user_playlists(user)

    if emotion == 'joy':
        song_name = 'Happy Hits!'
    elif emotion == 'surprise':
        song_name = 'Never Gonna Give You Up'
    elif emotion == 'sorrow':
        song_name = 'Mood Booster'
    elif emotion == 'anger':
        song_name = 'Hype'

    for i, playlist in enumerate(playlists['items'][0:4]):
        if song_name == playlist['name']:
            results = sp.playlist(playlist['id'], fields="tracks,next")
            tracks = results['tracks']
    return show_tracks(tracks)
