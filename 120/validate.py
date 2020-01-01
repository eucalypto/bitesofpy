from functools import wraps


def int_args(func):

    @wraps(func)
    def wrapped(*args):
        if any(type(arg) != int for arg in args):
            raise TypeError
        if any(arg < 0 for arg in args):
            raise ValueError
        return func(*args)

    return wrapped
