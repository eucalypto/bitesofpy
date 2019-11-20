from fizzbuzz import fizzbuzz

import pytest


# write one or more pytest functions below, they need to start with test_

@pytest.mark.parametrize(
    "input, expected",
    list(enumerate([1, 2, 'Fizz', 4, 'Buzz', "Fizz", 7, 8,
                    "Fizz" , "Buzz", 11, "Fizz", 13, 14,
                    "Fizz Buzz", 16, 17, "Fizz", 19,
                    "Buzz"],
                   start=1))
)
def test_fizzbuzz_first_20(input, expected):
    assert fizzbuzz(input) == expected
