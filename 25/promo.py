import random

BITES = {6: 'PyBites Die Hard',
         7: 'Parsing dates from logs',
         9: 'Palindromes',
         10: 'Practice exceptions',
         11: 'Enrich a class with dunder methods',
         12: 'Write a user validation function',
         13: 'Convert dict in namedtuple/json',
         14: 'Generate a table of n sequences',
         15: 'Enumerate 2 sequences',
         16: 'Special PyBites date generator',
         17: 'Form teams from a group of friends',
         18: 'Find the most common word',
         19: 'Write a simple property',
         20: 'Write a context manager',
         21: 'Query a nested data structure'}
bites_done = {6, 10, 16, 18, 21}


class NoBitesAvailable(Exception):
    pass


class Promo:

    def __init__(self, bites_done=bites_done):
        self.bites_done = bites_done

    def _pick_random_bite(self):
        """
        Return random bite that is not done yet

        :raise NoBitesAvailable
            if there are no not-done bites
        """
        available_bites = [bite
                           for bite in BITES.keys()
                           if bite not in self.bites_done]
        if not available_bites:  # if available_bites empty
            raise NoBitesAvailable

        return random.choice(available_bites)

    def new_bite(self):
        """Returns new random bite and updates done bites"""
        next_bite = self._pick_random_bite()
        self.bites_done.add(next_bite)
        return next_bite


if __name__ == '__main__':
    promo = Promo()
    print(promo._pick_random_bite())
