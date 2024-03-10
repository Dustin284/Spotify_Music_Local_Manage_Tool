import spotipy
from spotipy.oauth2 import SpotifyOAuth
from utils.Credentials import client_id, client_secret, redirect_uri
def get_artist_info(artist_name):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id, client_secret, redirect_uri))

    search_result = sp.search(q=artist_name, type="artist")

    artist_info = search_result["artists"]["items"][0]
    profile_image_url = artist_info["images"][0]["url"]

    print(f"Künstlername: {artist_info['name']}")
    print(f"Künstler-ID: {artist_info['id']}")
    print(f"Genres: {artist_info['genres']}")
    print(f"Followers: {artist_info['followers']['total']}")
    print(f"Profilbild-URL: {profile_image_url}")

    return artist_info
