from enum import Enum

THUMBS_UP = '👍'  # in case you go f-string ...


class Score(Enum):
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    def __str__(self):
        return f"{self.name} => {self.value * THUMBS_UP}"

    @classmethod
    def average(cls):
        return sum(member.value for member in Score) / len(Score)
