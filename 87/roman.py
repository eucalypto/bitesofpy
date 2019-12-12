def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""
    if type(decimal_number) != int:
        raise ValueError
    if not 0 < decimal_number < 4000:
        raise ValueError

    numerals = ["M", "CM", 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    roman_literal = ""
    for value, literal in zip(values, numerals):
        times = decimal_number // value
        roman_literal += times * literal
        decimal_number -= times * value
    return roman_literal
