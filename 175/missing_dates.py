import datetime

def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    start = min(dates)
    end = max(dates)

    missing = []
    iteration_day = start
    while iteration_day < end:
        if iteration_day not in dates:
            missing.append(iteration_day)
        iteration_day += datetime.timedelta(days=1)
    return missing
