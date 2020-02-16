num_hundreds = -1


def sum_numbers(numbers: list) -> int:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total"""
    summed_up = sum(numbers)
    global num_hundreds
    num_hundreds += summed_up // 100
    return summed_up
