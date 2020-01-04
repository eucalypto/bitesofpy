def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

       Examples - input -> output:
       '2 * 3' -> 6
       '2 + 6' -> 8

       Support +, -, * and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
    """
    num1, operation, num2 = calculation.split()
    if operation == '+':
        return int(num1) + int(num2)
    elif operation == '-':
        return int(num1) - int(num2)
    elif operation == '*':
        return int(num1) * int(num2)
    elif operation == '/':
        try:
            return int(num1) / int(num2)
        except ZeroDivisionError:
            raise ValueError
    else:
        raise ValueError

