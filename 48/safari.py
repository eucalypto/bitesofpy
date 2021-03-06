import os
import urllib.request

LOG = os.path.join('/tmp', 'safari.logs')
PY_BOOK, OTHER_BOOK = '🐍', '.'

urllib.request.urlretrieve('http://bit.ly/2BLsCYc', LOG)


def create_chart():
    """Read the log and make a text-based histogram of books pushed to slack for each day.
    Mark Python books with a'🐍'"""
    with open(LOG) as logfile:
        slack_entries = {}

        last_line = ""
        for line in logfile:
            if "sending to slack channel" in line:
                day = last_line[:5]
                if day not in slack_entries:
                    slack_entries[day] = ""
                slack_entries[day] += PY_BOOK if "python" in last_line.lower() else OTHER_BOOK

            last_line = line

        for day, books in slack_entries.items():
            print(day, books)


if __name__ == '__main__':
    create_chart()
