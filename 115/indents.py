def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    whitespace_count = 0
    for char in text:
        if char != " ":
            break
        whitespace_count += 1

    return whitespace_count


def test_count_indents():
    print(count_indents(" hello world  "))
    print(count_indents("    Gandalf the Grey"))


if __name__ == '__main__':
    test_count_indents()

