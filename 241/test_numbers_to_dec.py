import pytest

from numbers_to_dec import list_to_decimal


@pytest.mark.parametrize(
    'nums',
    [
        [0, 4, 2, 8],
        [1, 2],
        [7],
    ]
)
def test_not_raise_exceptions(nums):
    try:
        list_to_decimal(nums)
    except (ValueError, TypeError) as e:
        pytest.fail("Unexpetced " + str(e))


@pytest.mark.parametrize(
    'nums, expected',
    [
        ([0, 4, 2, 8], 428),
        ([1, 2], 12),
        ([7], 7),
    ]
)
def test_good_values(nums, expected):
    assert list_to_decimal(nums) == expected


@pytest.mark.parametrize(
    'nums, expected_error',
    [
        ([6, 2, True], TypeError),
        ([3.6, 4, 1], TypeError),
        (['4', 5, 3, 1], TypeError),
        ([-3, 12], ValueError),
        ([1, 10], ValueError),
        ([1, 42], ValueError),
        (42, TypeError),
        ('42', TypeError),
    ]
)
def test_raise_error(nums, expected_error):
    with pytest.raises(expected_error):
        assert list_to_decimal(nums)
