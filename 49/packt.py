from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

CONTENT = requests.get('http://bit.ly/2EN2Ntv').text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    page = Soup(CONTENT, features="html.parser")
    book = page.find(class_="dotd-main-book")

    title = book.find(class_="dotd-title").get_text().strip()

    description = book.find(class_="dotd-main-book-summary") \
        .contents[7].get_text().strip()

    image = book.find(class_="imagecache-dotd_main_image")["src"]

    link = book.find("a")["href"]

    return Book(title, description, image, link)


if __name__ == '__main__':
    print(get_book())
