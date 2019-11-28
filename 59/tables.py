class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self._table = [[i * j for j in range(0, length + 1)]
                       for i in range(0, length + 1)]
        # ↑ start the range with 0 so that we can later use the numbers as indices.
        # But in printing, the 0th row and column should be omitted.

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return (len(self._table) - 1) ** 2

    def __str__(self):
        """Returns a string representation of the table"""
        string = ""
        for row in self._table[1:]:
            string += " | ".join([str(number) for number in row[1:]]) \
                      + '\n'
        return string

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the re-calculated result"""
        return self._table[x][y]


if __name__ == '__main__':
    table = MultiplicationTable(3)
    print(table)
