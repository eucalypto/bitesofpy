class Animal:
    last_animal = 10000
    all_animals = []

    def __init__(self, name):
        self.name = name.capitalize()
        self.number = Animal.last_animal + 1
        Animal.last_animal = self.number
        Animal.all_animals.append(self)

    def __str__(self):
        return f'{self.number}. {self.name}'

    @classmethod
    def zoo(cls):
        return '\n'.join(str(animal) for animal in Animal.all_animals)
