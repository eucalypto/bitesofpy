WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    for row in range(size):
        out = ''
        if row % 2 == 0:
            for column in range(size):
                out += WHITE if column % 2 == 0 else BLACK
        else:
            for column in range(size):
                out += WHITE if column % 2 != 0 else BLACK
        print(out)

