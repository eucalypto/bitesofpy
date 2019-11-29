from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()

UnoCard = namedtuple('UnoCard', 'suit name')


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    colored_names = ["0"] \
        + 2 * "1, 2, 3, 4, 5, 6, 7, 8, 9, Skip, Reverse, Draw Two".split(sep=", ")
    uncolored_names = 4 * "Wild, Wild Draw Four".split(sep=", ")

    return [UnoCard(suit, name)
            for suit in SUITS
            for name in colored_names] \
        + [UnoCard(None, name)
            for name in uncolored_names]


if __name__ == '__main__':
    print(len(create_uno_deck()))
