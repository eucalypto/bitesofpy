import itertools


def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""

    not_common = [city
                  for city in (*my_cities, *other_cities)
                  if not (city in my_cities and city in other_cities)]
    return len(not_common)


# This is the pybites solution.
# It uses sets and the short syntax for symmetric_difference()
def uncommon_cities_from_pybites(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    return len(set(my_cities) ^ set(other_cities))
