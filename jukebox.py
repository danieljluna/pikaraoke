import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import logging

class Jukebox:
    
    spotify_scope = "user-read-playback-state,user-modify-playback-state"
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=spotify_scope, open_browser=True, client_id="6dda6a411d1e4c4cac29b7a194af860c", client_secret="0b1a85c52b15467db4ef1c0c71e6a5ea", redirect_uri="https://boguscallback.com/login"))
    is_paused = False

    def play(self):
        if self.is_paused:
            logging.info("Playing Spotify...")
            self.spotify.start_playback()
        self.is_paused = False

    def pause(self):
        if not self.is_paused:
            logging.info("Pausing Spotify...")
            self.spotify.pause_playback()
        self.is_paused = True
    