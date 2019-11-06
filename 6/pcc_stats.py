"""Checks community branch dir structure to see who submitted most
   and what challenge is more popular by number of PRs"""
from collections import Counter, namedtuple
import os
import urllib.request

# prep

tempfile = os.path.join('/tmp', 'dirnames')
urllib.request.urlretrieve('http://bit.ly/2ABUTjv', tempfile)

IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.split()

users, popular_challenges = Counter(), Counter()

Stats = namedtuple('Stats', 'user challenge')


#  code

def get_submissions_from_file(file_=tempfile):
    """Return a generator of (bite, user) submissions
       read from file_

       file_ is assumed to have this format:

       challenge<int>/file_or_dir<str>,is_dir<bool>
       03/rss.xml,False
       03/tags.html,False
       ...
       03/mridubhatnagar,True
       03/aleksandarknezevic,True

       -> use last column to filter out directories (= True)
    """
    with open(file_) as file:
        lines = file.readlines()

    for line in lines:
        longname, is_directory = line.rstrip("\n").split(",")
        if not is_directory == "True":
            continue
        bite, user = longname.split("/")
        yield bite, user


def diehard_pybites():
    """Return a Stats namedtuple (defined above) that contains the user that
       made the most PRs (ignoring the users in IGNORE) and a challenge tuple
       of most popular challenge and the amount of PRs for that challenge.
       Calling this function on the dataset (held tempfile) should return:
       Stats(user='clamytoe', challenge=('01', 7))
    """
    for bite, user in get_submissions_from_file():
        if user in IGNORE:
            continue
        users.update([user])
        popular_challenges.update([bite])

    return Stats(user=users.most_common(1)[0][0],
                 challenge=popular_challenges.most_common(1)[0]
                 )


def test_run():
    for submission in get_submissions_from_file():
        print(submission)
    print(diehard_pybites())
