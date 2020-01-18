import bisect


class OrderedList:

    def __init__(self):
        self._numbers = []

    def add(self, num):
        right_place = bisect.bisect_left(self._numbers, num)
        self._numbers.insert(right_place, num)

    def __str__(self):
        return ', '.join(str(num) for num in self._numbers)
