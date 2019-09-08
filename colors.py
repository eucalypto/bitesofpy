# Bite 102. Infinite loop, input, continue and break
# https://codechalleng.es/bites/102/

VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check:
       - if 'quit' was entered for color, print 'bye' and break.
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    while True:
        userinput = input().lower()
        if userinput == "quit":
            print("bye")
            break
        elif userinput in VALID_COLORS:
            print(userinput)
        else:
            print("Not a valid color")


if __name__ == '__main__':
    print_colors()
