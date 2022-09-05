import requests
from bs4 import BeautifulSoup

def get_soup(url):
    return BeautifulSoup(requests.get(url).text, "html.parser")

URL = "https://fidilio.com/coffeeshops"
soup = get_soup(URL)


cities = [x["value"] for x in \
    soup.find("select", attrs={"id":"cityClass"})\
    .find_all("option")]

for city in cities:

    city_url = f"{URL}/in/{city}"
    city_soup = get_soup(city_url)

    pages = int(city_soup.find("div", attrs={"class": "pagination"})\
            .find_all('a')[-1]["href"]\
            .split("=")[-1])

    for page in range(pages+1):
        page_url = f"{URL}/in/{city}/?page={page}"
        page_soup = get_soup(page_url)

        items = page_soup.find("div", attrs={"class": "restaurant-list-container"})\
            .find_all("a", attrs={"class": "restaurant-link"})

        for item in items:
            item_link = URL + item["href"].replace("coffeeshops/","")
            item_soup = get_soup(item_link)

            cafe_name = item_soup.find("h1", attrs={"property": "name"}).text.strip()

