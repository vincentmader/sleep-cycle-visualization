from datetime import datetime as dt
from datetime import timedelta as td

import numpy as np

from utils.dates import get_all_dates


class TimeSeries:
    def __init__(
        self,
        dates: np.ndarray,
        values: np.ndarray
    ):
        self.dates = dates
        self.values = values

    def __add__(self, rhs):
        return TimeSeries(self.dates, self.values + rhs)

    def __mul__(self, rhs):
        return TimeSeries(self.dates, self.values * rhs)

    def __rmul__(self, lhs):
        return self * lhs

    def __div__(self, rhs):
        return TimeSeries(self.dates, self.values / rhs)

    @property
    def average(self):
        return np.mean(self.values)

    def moving_average(self, N):
        i_start = get_idx_of_first_not_none_entry(self.values)

        mavg = np.array([])
        for i, date in enumerate(self.dates):
            M = 0
            S = 0
            for j in range(N):
                value = self.values[max(0, i - j)]
                if value != None:
                    M += 1
                    S += value
            val = S / M if M > 0 else None
            # val = correct_for_start(i, val, i_start, N)
            val = correct_for_portugal(date, val, N)
            mavg = np.append(mavg, val)
        return TimeSeries(self.dates, mavg)


def correct_for_start(idx, value, idx_start, N):
    if idx < idx_start + N:
        return None
    return value


def get_idx_of_first_not_none_entry(values):
    for i, value in enumerate(values):
        if value != None:
            return i


def correct_for_portugal(date, value, N):
    PORTUGAL_START = dt(2021, 1, 13)
    PORTUGAL_END = dt(2021, 5, 31)
    if PORTUGAL_START < date + td(days=N) < PORTUGAL_END:
        return None
    if PORTUGAL_START < date - td(days=N) < PORTUGAL_END:
        return None
    return value


def initialize_timeseries(initial_value=None):
    # return {date: initial_value for date in get_all_dates()}
    dates = get_all_dates()
    values = np.array([initial_value for d in dates])
    return TimeSeries(dates, values)


def initialize_timeseries_dict(initial_value=None):
    return {date: initial_value for date in get_all_dates()}


def moving_sum(arr, N):
    y = []
    for i, _ in enumerate(arr):
        y_i = 0
        for j in range(min(i, N)):
            y_i += arr[i - j]
        y.append(y_i)
    return np.array(y)


def moving_avg(arr, N):
    y = moving_sum(arr, N)
    return y / N


# def moving_avg_normalized(arr, N):
#     y_msum = moving_sum(arr, N)

#     timeseries = load_sleepcycle_usage_from_file()
#     dates = sorted(timeseries.keys())
#     sc_usage_bools = [timeseries[date] for date in dates]

#     sc_usage_ints = [{True: 1, False: 0}[b] for b in sc_usage_bools]
#     sc_usage_msum = moving_sum(sc_usage_ints, N)

#     return np.array([
#         y_msum[i] / sc_usage_msum[i]
#         if sc_usage_msum[i] > 0 else None
#         for i in range(len(y_msum))
#     ])
