from functools import wraps


def make_html(element):
    def decorator(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            """wrapper function"""
            return f"<{element}>" \
                   + func(*args, **kwargs) \
                + f"</{element}>"
        return wrap
    return decorator


if __name__ == '__main__':
    @make_html("p")
    def get_foo(text):
        """get_foo function"""
        return text

    def return_hello():
        return "hello"

    @make_html("bacon")
    def return_nothing():
        pass

    print(get_foo("hello"))
    return_hello = make_html("div")(return_hello)
    print(return_hello())
    print(get_foo)
    print(get_foo.__name__)
    print(help(get_foo))

    print(return_nothing())
