import requests
from bs4 import BeautifulSoup
import re

def get_soup(url) -> BeautifulSoup:
    return BeautifulSoup(requests.get(url).text, "html.parser")


def get_cities(soup: BeautifulSoup):
    return [x["value"] for x in \
            soup.find("select", attrs={"id":"cityClass"})\
            .find_all("option")]


def get_pages(city_soup: BeautifulSoup):
    return int(city_soup.find("div", attrs={"class": "pagination"})\
                .find_all('a')[-1]["href"]\
                .split("=")[-1])


def get_items(page_soup: BeautifulSoup):
    return page_soup.find("div", attrs={"class": "restaurant-list-container"})\
            .find_all("a", attrs={"class": "restaurant-link"})


def item_attrs(item_url, city) -> dict:
    item = {}
    item_soup = get_soup(item_url)

    item["name"] = item_soup.find("h1", attrs={"property": "name"}).text.strip()
    item["city"] = city
    item["link"] = item_url
    item["address"] = item_soup.find("span", attrs={"property": "address"}).text.strip()
    item["province"] = item["address"].split("،")[0].strip()
    item["phone"] = item_soup.find("span", attrs={"property": "telephone"}).find('a').text.strip()
    item["price_class"] = int(item_soup.find("div", attrs={"class": "price-class"}).find_all("span")[-1].text)
    _work_time = re.findall( r"[0-9:]+",
                    item_soup.find("ul", attrs={"class": "infolist"})\
                    .find_all("li")[-4]\
                    .find_all("span")[-1].text.strip())
    item["work_start"] = _work_time[0]
    item["work_end"] = _work_time[1]
    item["feature_list"] = [i.text for i in item_soup\
                            .find("div", attrs={"class": "venue-features-box"}).find_all("span")]
    _rates = item_soup.find("ul", attrs={"class": "rates-list"}).find_all("li")
    item["food_quality"] = int(_rates[0].div["data-rateit-value"])
    item["service"] = int(_rates[1].div["data-rateit-value"])
    item["cost_value"] = int(_rates[2].div["data-rateit-value"])
    item["environment"] = int(_rates[3].div["data-rateit-value"])
    return item


def scrape() -> list[dict]:
    result = []

    URL = "https://fidilio.com/coffeeshops"
    soup = get_soup(URL)
    cities = get_cities(soup)
    for city in cities:
        pages = get_pages(get_soup(f"{URL}/in/{city}"))
        for page in range(pages+1):
            items = get_items(get_soup(f"{URL}/in/{city}/?page={page}"))
            for item in items:
                item_url = URL + item["href"].replace("coffeeshops/","")
                result.append(item_attrs(item_url, city))
    return result


if __name__ == "__main__":
    result = scrape()