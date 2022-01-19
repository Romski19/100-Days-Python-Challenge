import os
import requests
import spotipy
import re
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup


CLIENT_ID = os.environ['SPOTIFY_CID']
CLIENT_SECRET = os.environ['SPOTIFY_SECRET']

user_input = input("Throwback Music Year? Fomrat(YYYY-MM-DD): ")
BB_URL = "https://www.billboard.com/charts/hot-100/"

response = requests.get(f"{BB_URL}/{user_input}")
songs = response.text


soup = BeautifulSoup(songs, "html.parser")

songs = soup.select("li h3")
song_titles = [song.getText().strip("\n") for song in songs[:10]]
    

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="./Day - 46/token.txt"))

user_id = sp.current_user()['id']

song_uris = []
year = user_input.split("-")[0]

for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify")



playlist = sp.user_playlist_create(user=user_id,
                        name=f"{user_input} Billboard Top 100",
                        public=False,
                        collaborative=False,
                        description=f"{user_input} Billboard Top 100")

sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['external_urls']['spotify'], tracks=song_uris)
