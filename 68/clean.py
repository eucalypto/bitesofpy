import string


def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    return "".join([char for char in input_string
                    if char not in string.punctuation])


if __name__ == '__main__':
    print(remove_punctuation("hello, dear.!"))
    print(remove_punctuation("!!!Yolo!!!Joe!!!.:)"))
