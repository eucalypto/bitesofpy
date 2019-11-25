from datetime import datetime

# https://pythonclock.org/
PY2_DEATH_DT = datetime(year=2020, month=1, day=1)
BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')


def py2_earth_hours_left(start_date=BITE_CREATED_DT):
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth (calculated from start_date)"""
    difference = round((PY2_DEATH_DT - start_date).total_seconds() / 3600,
                       ndigits=2)
    return difference


def py2_miller_min_left(start_date=BITE_CREATED_DT):
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller (calculated from start_date)"""
    earth_to_miller = 1 / (7 * 365 * 24)
    return round((PY2_DEATH_DT - start_date).total_seconds() / 60 * earth_to_miller,
                 ndigits=2)


def play_around():
    difference = (PY2_DEATH_DT - BITE_CREATED_DT).total_seconds() / 3600
    print(type(difference))
    print(difference)
    print(py2_earth_hours_left())


if __name__ == '__main__':
    play_around()
