def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    max_with = rows*2-1
    each_row = [((row*2-1) * '*').center(max_with)
                for row in range(1, rows+1)]

    return '\n'.join(each_row)


def test():
    print(generate_xmas_tree(4).split('\n'))
    print(generate_xmas_tree())

if __name__ == '__main__':
    test()
