import numpy as np


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
