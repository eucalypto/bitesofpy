from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    date = PYBITES_BORN
    next_anniversary = PYBITES_BORN.replace(year=PYBITES_BORN.year + 1)
    for _ in range(100):
        date += timedelta(days=100)
        if date < next_anniversary:
            yield date
        else:
            output = next_anniversary
            date -= timedelta(days=100)  # roll back for next yield
            next_anniversary = next_anniversary.replace(year=next_anniversary.year + 1)
            yield output

if __name__ == '__main__':
    dates = gen_special_pybites_dates()
    print(next(dates))
    print(next(dates))
    print(next(dates))
    print(next(dates))
    print(next(dates))
    print(next(dates))
    print(next(dates))
    print(next(dates))
    print(next(dates))
    print(next(dates))
    print(next(dates))

