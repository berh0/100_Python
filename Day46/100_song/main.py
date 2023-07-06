import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

soup = BeautifulSoup(response.text, "html.parser")
div_tags = soup.find_all("div", class_="o-chart-results-list-row-container")

title_list = []
for div_tag in div_tags:
    li_tag = div_tag.find("li", class_="lrv-u-width-100p")
    h3_tag = li_tag.find("h3").getText().split()
    title_song = " ".join(h3_tag)
    title_list.append(title_song)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        show_dialog=True,
        cache_path="token.txt",
        username="YOUR_USERNAME", 
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in title_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        pprint(f"{song} doesn't exist in Spotify. Skipped.")

pprint(song_uris)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
pprint(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris) 
