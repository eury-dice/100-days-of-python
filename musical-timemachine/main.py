from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import os

CLIENT_ID = os.environ["SPOTIFY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIFY_CLIENT_SECRET"]
REDIRECT_URI = os.environ["SPOTIFY_REDIRECT_URI"]

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year would you like to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]

date_url = BILLBOARD_URL + date

response_text = requests.get(date_url).text

soup = BeautifulSoup(response_text, "lxml")
chart = soup.find_all(name="span", class_="chart-element__information__song")
songs = [song.getText() for song in chart]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"))

user_id = sp.current_user()["id"]
song_uris = []

for song in songs:
    query = f"track:{song} year:{year}"
    result = sp.search(q=query, type="track", limit=1)
    try:
        song_uris.append(result['tracks']['items'][0]['uri'])
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist_name = f"{date} Billboard 100"
playlist_id = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)["id"]
res = sp.playlist_add_items(playlist_id, song_uris)
