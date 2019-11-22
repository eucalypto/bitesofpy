def round_even(number):
    """Takes a number and returns it rounded even"""
    integer_part = int(number)
    decimal_part = number - integer_part
    if integer_part % 2 == 0:
        if decimal_part <= 0.5:
            return integer_part
        else:
            return integer_part + 1
    else:
        if decimal_part < 0.5:
            return integer_part
        else:
            return integer_part + 1
