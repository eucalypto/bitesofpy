import datetime
import pytz

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones: str) -> bool:
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    try:
        timezones = [pytz.timezone(timezone)
                     for timezone in timezones]
    except pytz.UnknownTimeZoneError:
        # Pytz raises UnknownTimezoneError if it does not know a given
        # timezone
        raise ValueError("One of the timezones is unknown")

    utc_time = pytz.utc.localize(utc)

    for timezone in timezones:
        local_hour = utc_time.astimezone(timezone).hour
        if local_hour not in MEETING_HOURS:
            return False
    return True


if __name__ == '__main__':
    dt = datetime.datetime(2018, 4, 18, 13, 28)
    timezones = ["non-existing-timezone", 'Europe/Madrid', 'Australia/Sydney', 'America/Chicago']
    print(within_schedule(dt, *timezones))

