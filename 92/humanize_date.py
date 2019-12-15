from collections import namedtuple
from datetime import datetime

TimeOffset = namedtuple('TimeOffset', 'offset date_str divider')

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60*60, 24*60*60
TIME_OFFSETS = (
    TimeOffset(10, 'just now', None),
    TimeOffset(MINUTE, '{} seconds ago', None),
    TimeOffset(2*MINUTE, 'a minute ago', None),
    TimeOffset(HOUR, '{} minutes ago', MINUTE),
    TimeOffset(2*HOUR, 'an hour ago', None),
    TimeOffset(DAY, '{} hours ago', HOUR),
    TimeOffset(2*DAY, 'yesterday', None),
)


def pretty_date(date: datetime):
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    if type(date) != datetime:
        raise ValueError
    if date > NOW:
        raise ValueError

    difference = (NOW - date).total_seconds()
    for time_offset in TIME_OFFSETS:
        if difference < time_offset.offset:
            from_seconds = int(difference) if time_offset.divider is None \
                           else int(difference / time_offset.divider)
            return time_offset.date_str.format(from_seconds)
    return date.strftime('%m/%d/%y')

