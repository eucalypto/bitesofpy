import collections
from functools import wraps
from time import time
from typing import Deque, List, Set, Generator


def timing(f):
    """A simple timer decorator to print the elapsed time of
       the execution of the function it wraps.
       Returns (timing, result) tuple"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        duration = end - start
        print(f'Elapsed time {f.__name__}: {duration}')
        return duration, result
    return wrapper


@timing
def contains(sequence: List[int], num: int) -> bool:
    for n in sequence:
        if n == num:
            return True
    return False


@timing
def contains_fast(sequence: Set[int], num: int) -> bool:
    return num in sequence


@timing
def ordered_list_max(sequence: List[int]) -> int:
    return max(sequence)


@timing
def ordered_list_max_fast(sequence: List[int]) -> int:
    # List.sort() is apparently faster than max()
    # https://stackoverflow.com/questions/35014951/why-is-max-slower-than-sort
    # max() uses generic iteration and thus can be used with many
    # structures.
    # List.sort() does know that the underlying data is a list and thus
    # leverages this as a speed advantage.
    sequence.sort()

    # return sorted(sequence)[-1]
    # ↑ This is a bit slower than max() according to the test. Probably
    # because it has to generate a new list.

    return sequence[-1]


@timing
def list_concat(sequence: List[str]) -> str:
    bigstr = ''
    for i in sequence:
        bigstr += str(i)
    return bigstr
    # This is slow because strings are not mutable and each iteration
    # a new string object has to be created


@timing
def list_concat_fast(sequence: List[str]) -> str:
    return "".join(sequence)


@timing
def list_inserts(n: int) -> List[int]:
    lst = []
    for i in range(n):
        lst.insert(0, i)
    return lst


@timing
def list_inserts_fast(n: int) -> Deque[int]:
    # The deque (or double ended queue) is great for manipulations at both
    # ends. If you want to add an element in the beginning of a List, Python
    # shifts all later elements by one index. This is very inefficient.
    deque = collections.deque()
    for i in range(n):
        deque.insert(0, i)
    return deque


@timing
def list_creation(n: int) -> List[int]:
    lst = []
    for i in range(n):
        lst.append(i)
    return lst


@timing
def list_creation_fast(n: int) -> Generator[int, None, None]:
    return (i for i in range(n))
    # return range(n)
    # ^ this also passes the test since range() is a "sort of generator"
    # But the typing does not recognize it. The type of range is "range"
    # and the type check complains that it is not a generator.
