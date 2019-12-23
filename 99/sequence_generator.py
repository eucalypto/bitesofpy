from itertools import cycle
import string


def sequence_generator():
    return cycle(i
                 for tuple_ in zip(range(1, 27), string.ascii_uppercase)
                 for i in tuple_)
