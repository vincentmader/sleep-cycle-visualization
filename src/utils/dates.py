from datetime import datetime as dt
from datetime import timedelta as td

import numpy as np

from config import START_DATE
from config import END_DATE


def get_date_from_str(string):
    return dt.strptime(string, "%Y-%m-%d %H:%M:%S")


def get_all_dates():
    nr_of_days = (END_DATE - START_DATE).days
    days = [START_DATE + td(days=i) for i in range(nr_of_days)]
    return np.array(days)
