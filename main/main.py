import spotipy
from spotipy.oauth2 import SpotifyOAuth
from utils.Credentials import client_id, client_secret, redirect_uri
from methods.getArtist import get_artist_info
from methods.getTrack import get_track_info

def main():
    song2 = "500PS"
    song = get_track_info(song2)

if __name__ == "__main__":
    main()