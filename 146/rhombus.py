STAR = '*'

def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """
    for stars in range(1, width+1, 2):
        yield ('*' * stars).center(width)
    for stars in range(width-2, 0, -2):
        yield ('*' * stars).center(width)
