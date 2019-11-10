def positive_divide(numerator, denominator):
    try:
        result = numerator/denominator
    except ZeroDivisionError:
        result = 0
    if result < 0:
        raise ValueError("No negative results allowed")
    return result
