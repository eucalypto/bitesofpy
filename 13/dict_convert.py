from collections import namedtuple
from datetime import datetime
import json

blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here

blog_nt = namedtuple("Blog", "name, founders, started, tags, location, site")


def dict2nt(dict_):
    # return blog_nt._make(blog.values())
    return blog_nt(**blog)


def nt2json(nt: blog_nt):
    # Without the following default=str, you get the error:
    #   TypeError: Object of type datetime is not JSON serializable
    # default takes a default conversion function for objects that
    # json can't convert itself. Here, I just used the string
    # conversion function.
    return json.dumps(nt._asdict(), default=str)


if __name__ == '__main__':
    print(nt2json(dict2nt(blog)))
