def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if not (type(value) == int or type(value) == float):
        raise TypeError("Type of the input must be numeric: int or float")
    if not (fmt.casefold() == 'cm' or fmt.casefold() == 'in'):
        raise ValueError("Type must be either 'cm' or 'in'")

    cm_per_inch = 2.54

    if fmt.casefold() == 'in':
        return round(value / cm_per_inch, ndigits=4)
    elif fmt.casefold() == 'cm':
        return round(value * cm_per_inch, ndigits=4)
