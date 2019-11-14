import pytest
from omdb import (get_movie_data, get_single_comedy,
                  get_movie_most_nominations, get_movie_longest_runtime,
                  get_runtime, get_nominations)

movies = get_movie_data()


def test_movie_data_structure():
    assert len(movies) == 5
    assert all(type(m) == dict for m in movies)


def test_data_analysis():
    assert get_single_comedy(movies) == 'Horrible Bosses'
    assert get_movie_most_nominations(movies) == 'Fight Club'
    assert get_movie_longest_runtime(movies) == 'Blade Runner 2049'


@pytest.mark.parametrize(
    "movie, expected_runtime",
    zip(movies, [98, 107, 139, 164, 100])
    # [(movie[0], 98), (movie[1], 107), ...]
)
def test_get_runtime(movie, expected_runtime):
    assert get_runtime(movie) == expected_runtime


@pytest.mark.parametrize(
    "movie, expected_nominations",
    zip(movies, [11, 6, 32, 13, 10])
)
def test_get_nominations(movie, expected_nominations):
    assert get_nominations(movie) == expected_nominations
