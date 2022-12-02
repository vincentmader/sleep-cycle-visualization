import numpy as np

from utils.dates import get_all_dates


class TimeSeries:
    # def __init__(self, dates=None, values=None):
    def __init__(self, dates, values):
        # if dates == None:
        #     dates = get_all_dates()
        # if values == None:
        #     values = np.array([None for _ in dates])
        # elif values == False:
        #     values = np.array([None for _ in dates])
        # if dates.shape == values.shape:
        #     raise Exception("shape mismatch in TimeSeries definition")
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

    def moving_average(self, N):
        mavg = []
        for i, _ in enumerate(self.dates):
            M = 0
            S = 0
            for j in range(N):
                value = self.values[i - j]
                if value != None:
                    M += 1
                    S += value
            mavg.append(S / M)
        return TimeSeries(self.dates, mavg)


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
