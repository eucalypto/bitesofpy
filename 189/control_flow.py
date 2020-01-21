IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    yield_count = 0
    for name in names:
        if name.startswith(IGNORE_CHAR):
            continue
        if not name.isalpha():
            continue
        if name.startswith(QUIT_CHAR):
            break
        if yield_count >= MAX_NAMES:
            break
        yield_count += 1
        yield name
