import random

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
aliases = 'Pythonista Nerd Coder'.split() * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def generate_table(*sequences):
    rows = []
    for row_items in zip(*sequences):
        row_items_as_strings = map(str, row_items)
        rows.append(SEPARATOR.join(row_items_as_strings))
    return rows


if __name__ == '__main__':
    print(generate_table(names, aliases, points, awake))
