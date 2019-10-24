from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    dates = []
    date = PYBITES_BORN
    next_anniversary = PYBITES_BORN.replace(year=PYBITES_BORN.year + 1)
    for i in range(10):
        date += timedelta(days=100)
        if date < next_anniversary:
            dates.append(date)
        else:
            dates.append(next_anniversary)
            dates.append(date)
            next_anniversary = next_anniversary.replace(year=next_anniversary.year + 1)
    return dates
