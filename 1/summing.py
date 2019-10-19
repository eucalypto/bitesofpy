def sum_numbers(numbers=None):
    if numbers is None:
        return sum_numbers(list(range(1, 101)))

    output = 0
    for number in numbers:
        output += number
    return output
