from datetime import datetime
import inspect
import pytest
from typing import Callable

from top_n import (numbers, dates, earnings_mln,
                   get_largest_number, get_latest_dates,
                   get_highest_earnings)


@pytest.mark.parametrize(
    "function, input_data, n, expected_output", [
        (get_largest_number, numbers, None, [6, 5, 4]),
        (get_largest_number, numbers, 2, [6, 5]),
        (get_largest_number, numbers, 4, [6, 5, 4, 3]),
        (get_latest_dates, dates, None, [datetime(2019, 2, 27, 0, 0),
                                         datetime(2018, 12, 19, 0, 0),
                                         datetime(2018, 11, 19, 0, 0)]),
        (get_latest_dates, dates, 1, [datetime(2019, 2, 27, 0, 0)]),
        (get_highest_earnings, earnings_mln, None, [{'name': 'Beyoncé Knowles',
                                                     'earnings': 105},
                                                    {'name': 'J.K. Rowling',
                                                     'earnings': 95},
                                                    {'name': 'Cristiano Ronaldo',
                                                     'earnings': 93}]),
    ]
)
def test_get_top_n(function: Callable, input_data, n, expected_output):
    if n is None:
        assert function(input_data) == expected_output
    else:
        assert function(input_data, n=n) == expected_output


def test_heapq_used():
    err_msg = 'We want you to play with heapq for this one :)'
    assert 'heapq' in inspect.getsource(get_largest_number), err_msg
    assert 'heapq' in inspect.getsource(get_latest_dates), err_msg
    assert 'heapq' in inspect.getsource(get_highest_earnings), err_msg
