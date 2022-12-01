from datetime import datetime as dt
from datetime import timedelta as td

from config import START_DATE


def get_date_from_str(string):
    return dt.strptime(string, "%Y-%m-%d %H:%M:%S")


def prepare_empty_timeseries(initial_value=None):
    """Create empty time-series object.

    Returns:
        dict(int: None)

        Format: {
            unix_timestamp: None,
            ...
        }
    """

    # Initialize time-axis.
    nr_of_days = (dt.now() - START_DATE).days
    days = [START_DATE + td(days=i) for i in range(nr_of_days)]

    # Initialize for all dates.
    timeseries = {d.timestamp(): initial_value for d in days}

    return timeseries
