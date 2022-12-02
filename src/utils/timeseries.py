import numpy as np

from utils.dates import get_all_dates

def initialize_timeseries(initial_value=None):
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
