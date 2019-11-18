import operator
import os
import re
import urllib.request
from datetime import timedelta
from functools import reduce

# getting the data
COURSE_TIMES = os.path.join('/tmp', 'course_timings')
urllib.request.urlretrieve('http://bit.ly/2Eb0iQF', COURSE_TIMES)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    with open(COURSE_TIMES) as file:
        courses_raw = file.read()
    return re.findall(r'\(([0-9]{1,2}:[0-9]{2})\)',
                      # regex matches "(3:47)" or "(10:27)"
                      # and returns "3:47" or "10:27" (by using parenthesis)
                      courses_raw)


def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""

    def to_timedelta(time_str):
        minutes, seconds = time_str.split(":")
        return timedelta(minutes=int(minutes),
                         seconds=int(seconds))

    summed_times = reduce(operator.add,
                          (to_timedelta(timestamp)
                           for timestamp in timestamps))
    return str(summed_times)


if __name__ == '__main__':
    print(get_all_timestamps(), len(get_all_timestamps()))
    print(calc_total_course_duration(get_all_timestamps()))
    time1 = timedelta(minutes=1, seconds=1)
    print(time1 + time1)
    # print(timedelta)
    # for i in calc_total_course_duration(get_all_timestamps()):
    #     print(i)
