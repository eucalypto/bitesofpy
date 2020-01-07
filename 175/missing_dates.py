from dateutil import rrule


def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    dates = set(dates)
    start = min(dates)
    end = max(dates)

    all_dates = set(dt.date()
                    for dt in
                    rrule.rrule(rrule.DAILY, start, until=end))
    return all_dates - dates
