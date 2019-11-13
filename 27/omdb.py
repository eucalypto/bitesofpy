import glob
import json
import os
from urllib.request import urlretrieve

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
    most_nominations = 0
    movie = None
    for movie in movies:
        awards = movie["Awards"]
    



def get_movie_longest_runtime(movies):
    pass


if __name__ == '__main__':
    movies = get_movie_data()
    # print(get_single_comedy(movies))
    get_movie_most_nominations(movies)
