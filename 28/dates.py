import collections
from datetime import datetime
import os
import re
from urllib.request import urlretrieve

BASE_URL = 'http://projects.bobbelderbos.com/pcc/dates/'
RSS_FEED = 'all.rss.xml'
PUB_DATE = re.compile(r'<pubDate>(.*?)</pubDate>')
TMP = '/tmp'


def _get_dates():
    """Downloads PyBites feed and parses out all pub dates returning
       a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
       'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""
    remote = os.path.join(BASE_URL, RSS_FEED)
    local = os.path.join(TMP, RSS_FEED)
    urlretrieve(remote, local)

    with open(local) as f:
        return PUB_DATE.findall(f.read())


def convert_to_datetime(date_str):
    """Receives a date str and convert it into a datetime object

    Example string: 'Sun, 07 Jan 2018 12:00:00 +0100'
    """
    return datetime.strptime(date_str, "%a, %d %b %Y %X %z")


def get_month_most_posts(dates):
    """Receives a list of datetimes and returns the month (format YYYY-MM)
       that occurs most"""
    months = collections.Counter(date.strftime("%Y-%m")
                                 for date in dates)
    return months.most_common(1)[0][0]


if __name__ == '__main__':
    date = convert_to_datetime('Sun, 07 Jan 2018 12:00:00 +0100')
    print(date.strftime("%Y-%m"))
    dates = (convert_to_datetime(date) for date in _get_dates())
    print(get_month_most_posts(dates))
