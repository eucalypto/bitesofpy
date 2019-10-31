import calendar
import datetime


def weekday_of_birth_date(date: datetime.date):
    """Takes a date object and returns the corresponding weekday string"""
    return calendar.day_name[date.weekday()]


if __name__ == '__main__':
    print(weekday_of_birth_date(datetime.date.today()))
    print(weekday_of_birth_date(datetime.date(1988, 8, 14)))
