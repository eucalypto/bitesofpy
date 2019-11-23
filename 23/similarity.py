import os
import re
from difflib import SequenceMatcher
import itertools
from urllib.request import urlretrieve

# prep
TAG_HTML = re.compile(r'<category>([^<]+)</category>')
TEMPFILE = os.path.join('/tmp', 'feed')
MIN_TAG_LEN = 10
IDENTICAL = 1.0
SIMILAR = 0.95

urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/tags.xml',
    TEMPFILE
)


def _get_tags(tempfile=TEMPFILE):
    """Helper to parse all tags from a static copy of PyBites' feed,
       providing this here so you can focus on difflib"""
    with open(tempfile) as f:
        content = f.read().lower()
    # take a small subset to keep it performant
    tags = TAG_HTML.findall(content)
    tags = [tag for tag in tags if len(tag) > MIN_TAG_LEN]
    return set(tags)


def get_similarities(tags=None):
    """Should return a list of similar tag pairs (tuples)"""
    tags = tags or _get_tags()
    # do your thing ...
    tags_remaining = {tag: True for tag in tags}
    pairs = set()
    for romeo in tags_remaining:
        for juliet in tags_remaining:
            if juliet == romeo:
                continue
            if SequenceMatcher(lambda x: x == " ", romeo, juliet).ratio() > 0.95:
                pairs.add(tuple(sorted([romeo, juliet])))
                tags_remaining[romeo] = False
                tags_remaining[juliet] = False

    return pairs


if __name__ == '__main__':
    print(get_similarities())
