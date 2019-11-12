from functools import wraps


def make_html(element):
    def decorator(func):
        def make_html_wrap(*args, **kwargs):
            return f"<{element}>" \
                   + func(*args, **kwargs) \
                + f"</{element}>"
        return make_html_wrap
    return decorator


@make_html("p")
def get_foo(text):
    return text


if __name__ == '__main__':
    print(get_foo("hello"))
