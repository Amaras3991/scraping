import requests
from bs4 import BeautifulSoup

URL = "https://au.rollingstone.com/100-greatest-movies-of-all-time/page/6/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("div", class_="c-list c-list--albums")
#print(results.prettify())
films = results.find_all("article", class_="c-list__item")
#print(films)
for film in films:
    title = film.find("h3", class_="c-list__title t-bold")
    film_info = film.find("p")
    print(title.text)
    print(film_info.text)
    print()