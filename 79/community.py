import csv
import requests

from collections import Counter

CSV_URL = 'https://bit.ly/2HiD2i8'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    return requests.get(CSV_URL).text


def create_user_bar_chart(content=get_csv()):
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    timezones = (entry.split(sep=",")[-1] for entry in content.splitlines()[1:])
    counter = Counter(timezones)
    for timezone, amount in counter.most_common():
        print(timezone.ljust(20) + "| " + amount * "+")


if __name__ == '__main__':
    # get_csv()
    create_user_bar_chart()
