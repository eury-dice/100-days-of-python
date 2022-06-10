from bs4 import BeautifulSoup
import requests

URL = "https://www.imdb.com/chart/top/"

response = requests.get(url=URL).text

soup = BeautifulSoup(response, "html.parser")

movie_titles = soup.select(selector="td.titleColumn a")

with open("movies.txt", "w") as file:
    for i in range(100):
        file.write(f"{i + 1}) {movie_titles[i].getText()}\n")
