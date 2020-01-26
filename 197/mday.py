from datetime import date
from dateutil import relativedelta as rd


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    return date(year, 5, 1) + rd.relativedelta(weekday=rd.SU(+2))
