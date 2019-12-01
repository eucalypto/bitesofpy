from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    def __init__(self, max_eggs):
        self.max_eggs = max_eggs
        self.eggs_produced = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.eggs_produced >= self.max_eggs:
            raise StopIteration
        self.eggs_produced += 1
        return f"{choice(COLORS)} egg"
