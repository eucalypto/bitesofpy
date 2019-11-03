import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies_by_director = {}
    with open(local) as csvfile:
        reader = csv.DictReader(csvfile)
        for entry in reader:
            director = entry.get("director_name")
            movie = Movie(entry.get("movie_title").strip(),
                          entry.get("title_year"),
                          entry.get("imdb_score"))
            if director in movies_by_director.keys():
                # update movies
                movies_by_director[director].append(movie)
            else:
                # Make new entry for director
                movies_by_director[director] = [movie]
    return movies_by_director


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    pass


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    pass


if __name__ == '__main__':
    print(get_movies_by_director())
