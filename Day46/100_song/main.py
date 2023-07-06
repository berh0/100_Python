import requests
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")

soup = BeautifulSoup(response.text, "html.parser")
div_tags = soup.find_all("div", class_="o-chart-results-list-row-container")
for div_tag in div_tags:
    li_tag = div_tag.find("li", class_="lrv-u-width-100p")
    h3_tag = li_tag.find("h3").getText().split()
    title_song = " ".join(h3_tag)
    print(title_song)