from collections import namedtuple
from datetime import datetime
import json
from typing import NamedTuple

blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here

Blog = namedtuple("Blog", blog.keys())


def dict2nt(dict_: dict):
    # return Blog._make(blog.values())
    return Blog(**blog)


def nt2json(nt: NamedTuple):
    # Without the following default=str, you get the error:
    #   TypeError: Object of type datetime is not JSON serializable
    # default takes a default conversion function for objects that
    # json can't convert itself. Here, I just used the string
    # conversion function.
    return json.dumps(nt._asdict(), default=str)


if __name__ == '__main__':
    print(nt2json(dict2nt(blog)))
