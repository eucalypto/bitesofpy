from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

CONTENT = requests.get('http://bit.ly/2EN2Ntv').text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    page = Soup(CONTENT, features="html.parser")
    title = page.find(class_="dotd-title")

    description = title.next_sibling.next_sibling\
        .next_sibling.next_sibling.text.strip()

    # print(page.prettify())

    image_obj = page.find(class_="imagecache-dotd_main_image")
    image = image_obj["src"]

    book = page.find(class_="dotd-main-book")
    # print(book.prettify())
    link = book.find("a")["href"]

    return Book(title.text.strip(), description, image, link)

if __name__ == '__main__':
    print(get_book())
