from dataclasses import dataclass

from dateutil import parser
from dateutil import relativedelta

@dataclass
class Actor:
    name: str
    born: str


@dataclass
class Movie:
    title: str
    release_date: str


def get_age(actor: Actor, movie: Movie) -> str:
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    born = parser.parse(actor.born)
    release = parser.parse(movie.release_date)
    difference = relativedelta.relativedelta(release, born)
    return f'{actor.name} was {difference.years} years old when {movie.title} came out.'
