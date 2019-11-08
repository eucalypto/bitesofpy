from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line: str):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    time_string = line.split()[1]
    return datetime.fromisoformat(time_string)


def time_between_shutdowns(loglines=loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    shutdown_times = [convert_to_datetime(line)
                      for line in loglines
                      if "Shutdown initiated." in line]

    start, stop = shutdown_times[:2]
    return stop - start

if __name__ == '__main__':
    print(convert_to_datetime("INFO 2014-07-03T23:27:51 supybot Shutdown complete."))
    print(time_between_shutdowns())
