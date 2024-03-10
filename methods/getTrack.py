import spotipy
from spotipy.oauth2 import SpotifyOAuth
from utils.Credentials import client_id, client_secret, redirect_uri

def get_track_info(track_name):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id, client_secret, redirect_uri))

    search_result = sp.search(q=track_name, type="track")

    if search_result['tracks']['items']:
        track_info = search_result['tracks']['items'][0]
        album_info = sp.album(track_info['album']['id'])
        artist_info = sp.artist(track_info['artists'][0]['id'])

        print(f"Track Name: {track_info['name']}")
        print(f"Track ID: {track_info['id']}")
        print(f"Album Name: {album_info['name']}")
        print(f"Album ID: {album_info['id']}")
        print(f"Artist Name: {artist_info['name']}")
        print(f"Artist ID: {artist_info['id']}")
        print(f"Release Date: {album_info['release_date']}")
        print(f"Genres: {artist_info['genres']}")
        print(f"Popularity: {track_info['popularity']}")
        # Fetch the first image from the album's images
        if album_info['images']:
            track_pic_url = album_info['images'][0]['url']
            print(f"Track Picture URL: {track_pic_url}")
    else:
        print("Track not found.")