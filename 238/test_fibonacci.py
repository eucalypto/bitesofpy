from fibonacci import fib
import pytest

# write one or more pytest functions below, they need to start with test_


@pytest.mark.parametrize(
    "index, expected",
    list(zip(range(1, 11), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]))
)
def test_fib_first_10_numbers(index, expected):
    assert fib(index) == expected


def test_fib_raises_error_for_negative_input():
    with pytest.raises(ValueError):
        assert fib(-1)
