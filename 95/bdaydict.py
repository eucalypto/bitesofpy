from datetime import date

MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __setitem__(self, name, birthday: date):
        birthdays = [(birthday_.day, birthday_.month) for birthday_ in self.values()]
        if (birthday.day, birthday.month) in birthdays:
            print(MSG.format(name))
        dict.__setitem__(self, name, birthday)
