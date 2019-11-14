import glob
import json
import os
from urllib.request import urlretrieve
import re

BASE_URL = 'http://projects.bobbelderbos.com/pcc/omdb/'
MOVIES = ('bladerunner2049 fightclub glengary '
          'horrible-bosses terminator').split()
TMP = '/tmp'

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f'{movie}.json'
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, '*json'))


def get_movie_data(files=files):
    movies = []
    for file_name in files:
        with open(file_name) as file:
            load = json.load(file)
        movies.append(load)
    return movies


def get_single_comedy(movies):
    for movie in movies:
        if "Comedy" in movie["Genre"]:
            return movie["Title"]


def get_movie_most_nominations(movies):
    most_nominations = max(movies, key=get_nominations)
    return most_nominations["Title"]


def get_nominations(movie: dict) -> int:
    """Return number of nominations of movie"""
    return int(re.findall(r"([0-9]*) nominations\.$",
                          movie["Awards"])[0])


def get_movie_longest_runtime(movies):
    longest = max(movies, key=get_runtime)
    return longest["Title"]


def get_runtime(movie: dict) -> int:
    """Return runtime of movie in minutes"""
    runtime_str = movie["Runtime"]
    return int(re.findall(r"([0-9]*) min",
                          runtime_str)[0])


if __name__ == '__main__':
    movies = get_movie_data()
    # print(movies)
    for movie in movies:
        # print(movie["Title"], movie["Runtime"])
        print(movie["Title"], movie["Awards"])
    # print(get_single_comedy(movies))
    # print(get_movie_most_nominations(movies))
    # print(get_movie_longest_runtime(movies))
