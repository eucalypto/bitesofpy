import itertools
from collections import OrderedDict

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = min(scores), max(scores)


def get_belt(user_score):
    if user_score < MIN_SCORE:
        return None
    reached_scores = list(filter(lambda score: score <= user_score, scores))
    return belts[len(reached_scores)-1]


if __name__ == '__main__':
    print(get_belt(10))
