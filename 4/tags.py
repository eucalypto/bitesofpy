import os
from collections import Counter
import urllib.request

import re
import feedparser

# prep

tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


# start coding

def get_pybites_top_tags(n=10):
    tag_search = re.compile(r"<category>([a-z]*)</category>")
    tags_counter = Counter(tag_search.findall(content))
    return tags_counter.most_common(n)


def get_pybites_top_tags_using_feedparser(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    # TODO: For some reason this function gives one single false count:
    # All counts are according to the tests EXCEPT "python". This function
    # gives a count of 78, whereas the tests expect 79.
    # Opening the raw xml file in an editor we see indeed 79 matches for
    # "<category>python</category>".
    # Solution: rewrite the function to just do a text search like the text
    # editor. ^-^

    feed = feedparser.parse(content)
    tags_counter = Counter()
    for entry in feed.entries:
        for tag in entry.tags:
            tags_counter.update([tag.term])
    return tags_counter.most_common(n)


def test_run():
    # print(get_pybites_top_tags().entries[0].tags[1].term)
    # print(get_pybites_top_tags_using_feedparser())
    print(get_pybites_top_tags())


if __name__ == '__main__':
    test_run()
