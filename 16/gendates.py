from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    date = datetime(2019, 11, 17)
    print(date.__repr__())
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


if __name__ == '__main__':
    dates = gen_special_pybites_dates()
    expected = [datetime(2017, 3, 29, 0, 0),
                datetime(2017, 7, 7, 0, 0),
                datetime(2017, 10, 15, 0, 0),
                datetime(2017, 12, 19, 0, 0),  # PyBites 1 year old
                datetime(2018, 1, 23, 0, 0),
                datetime(2018, 5, 3, 0, 0),
                datetime(2018, 8, 11, 0, 0),
                datetime(2018, 11, 19, 0, 0),
                datetime(2018, 12, 19, 0, 0),  # PyBites 2 years old
                datetime(2019, 2, 27, 0, 0)]
    print(dates)
    print(expected)
