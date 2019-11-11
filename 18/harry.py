import os
import urllib.request
import string
from collections import Counter

# data provided
stopwords_file = os.path.join('/tmp', 'stopwords')
harry_text = os.path.join('/tmp', 'harry')
urllib.request.urlretrieve('http://bit.ly/2EuvyHB', stopwords_file)
urllib.request.urlretrieve('http://bit.ly/2C6RzuR', harry_text)


def get_harry_most_common_word():
    with open(stopwords_file) as file:
        stopwords = [word.strip()
                     for word in file.readlines()]

    with open(harry_text) as file:
        lines = file.readlines()

    lines = [line.strip().lower() for line in lines]
    words = [strip_non_alphanumeric(word)
             for line in lines
             for word in line.split()
             if word not in stopwords]
    words = [word
             for word in words
             if word != ""]
    count = Counter(words)
    return count.most_common()[0]


def strip_non_alphanumeric(text: str):
    return "".join([char
                    for char in text
                    if char in (string.ascii_lowercase + string.digits)])


if __name__ == '__main__':
    print(strip_non_alphanumeric("2234 uiaern ;.iaren ;j uiae"))

    print(get_harry_most_common_word())
