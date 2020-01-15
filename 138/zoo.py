import itertools


class Animal:
    _id_count = itertools.count(10001)
    _all_animals = []

    def __init__(self, name):
        self.name = name.capitalize()
        self.id = next(Animal._id_count)
        Animal._all_animals.append(self)

    def __str__(self):
        return f'{self.id}. {self.name}'

    @classmethod
    def zoo(cls):
        return '\n'.join(str(animal) for animal in Animal._all_animals)
