from dataclasses import dataclass


@dataclass(order=True)
class Bite:
    number: int
    title: str
    level: str = 'Beginner'

    def __post_init__(self):
        """
        Dataclass automatically generates a wonderful __init__() constructor
        Here, we just want to adjust the constructor by capitalizing the title.
        We use this hook: __post_init__()
        :return:
        """
        self.title = self.title.capitalize()
