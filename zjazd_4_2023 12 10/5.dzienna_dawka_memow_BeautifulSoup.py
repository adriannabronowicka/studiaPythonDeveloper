import httpx
from bs4 import BeautifulSoup, Tag
from pathlib import Path

"""
Pobierz obrazki do folderu jpgs
Dodatkowe punkty za użycie async.gather
"""


def find_newest_page_number(xml_tag: Tag):
    tags_with_kwejk_href = xml_tag.find_all("a", attrs={"href": "https://kwejk.pl"})
    for tag in tags_with_kwejk_href:
        if tag.text.isnumeric():
            return int(tag.text)


def download_image(url: str, filename: str):
    response = httpx.get(url)
    jpg_file = open(Path(__file__).parent / "jpgs" / filename, "wb")
    jpg_file.write(response.content)


def download_newest_memes():
    response = httpx.get("https://kwejk.pl/")
    response.raise_for_status()
    html = BeautifulSoup(response.text, features="html.parser")
    images = html.find_all("img", attrs={"class": "full-image"})
    newest_page = find_newest_page_number(html)
    for image in images:
        image: Tag
        url = image.attrs["src"]
        name = image.attrs["src"][-9::]
        print(name)
        download_image(url, name)


download_newest_memes()

"""
Używając html.find znajdź aktualnie najnowszą stronę memów
"""
