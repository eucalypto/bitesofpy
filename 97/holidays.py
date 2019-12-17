from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup
import bs4


# prep data
tmp = os.getenv("TMP", "/tmp")
page = 'us_holidays.html'
holidays_page = os.path.join(tmp, page)
urlretrieve(
    f'https://bites-data.s3.us-east-2.amazonaws.com/{page}',
    holidays_page
)

with open(holidays_page) as f:
    content = f.read()




def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    holidays = defaultdict(list)
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find(class_="list-table").tbody
    for entry in table.children:
        # I hate this: table.children gives both Tag and NavigableString objects, so I have to manually
        # ignore the latter
        if isinstance(entry, bs4.element.NavigableString):
            continue
        name = entry.a.text.strip()
        month = entry.time['datetime'].split("-")[1]
        if month in holidays:
            holidays[month].append(name)
        else:
            holidays[month] = [name]
    return holidays

if __name__ == '__main__':
    get_us_bank_holidays()
