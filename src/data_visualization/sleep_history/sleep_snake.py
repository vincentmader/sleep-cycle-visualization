from datetime import timedelta as td
import os

import matplotlib.pyplot as plt
import numpy as np

from config import MPL_THEME
from config import PATH_TO_FIGURES
from config import PATH_TO_DATA
from utils.cprint import cprint
from utils.file_io import load_from_pickle
from utils.dates import get_all_dates
from utils.timeseries import moving_avg

N = 50


def foo(
    x, 
    list_measurement_start, 
    list_measurement_end,
    list_measurement_duration_in_s
):
    times = np.array([])
    measurement_starts_in_s = np.array([])
    measurement_ends_in_s = np.array([])
    measurement_durations_in_s = np.array([])
    for d in x:
        start = list_measurement_start[d]
        end = list_measurement_end[d]
        duration = list_measurement_duration_in_s[d]
        if start == None or duration == None:
            start, end, duration = 0, 0, 0
        else:
            start = start.hour * 3600\
                  + start.minute * 60\
                  + start.second
            end = end.hour * 3600\
                + end.minute * 60\
                + end.second
            if start > 18 * 3600:
                start -= 24 * 3600
            if end > 18 * 3600:
                end -= 24 * 3600
        times = np.append(times, d)
        measurement_starts_in_s = np.append(measurement_starts_in_s, start)
        measurement_ends_in_s = np.append(measurement_ends_in_s, start)
        measurement_durations_in_s = np.append(measurement_durations_in_s, duration)
    return times, measurement_starts_in_s, measurement_ends_in_s, measurement_durations_in_s


def plot_sleep_snake():
    cprint(" Plotting sleep-snake...")

    x = get_all_dates()

    path_to_savefiles = os.path.join(PATH_TO_DATA, "out", "sleep_history")

    path_to_savefile = os.path.join(path_to_savefiles, "measurement_start.p")
    list_measurement_start = load_from_pickle(path_to_savefile)
    path_to_savefile = os.path.join(path_to_savefiles, "measurement_end.p")
    list_measurement_end = load_from_pickle(path_to_savefile)
    path_to_savefile = os.path.join(path_to_savefiles, "measurement_duration_in_s.p")
    list_measurement_duration_in_s = load_from_pickle(path_to_savefile)

    dates, measurement_starts_in_s, measurement_ends_in_s, measurement_durations_in_s = foo(
        x, list_measurement_start, list_measurement_end, list_measurement_duration_in_s
    )

    plt.style.use(MPL_THEME)
    plt.figure(figsize=(16, 6))

    plt.bar(
        dates,
        measurement_durations_in_s/3600, 
        bottom=measurement_starts_in_s/3600, 
        width=td(days=1),
        color="gray"
    )
    # plt.plot(x, moving_avg(measurement_starts_in_s, N))
    # plt.plot(x, moving_avg(measurement_ends_in_s, N))

    plt.xlim(x[0], x[-1])
    plt.ylim(-3, 18) # ?

    plt.yticks(
        [-3, 0, 3, 6, 9, 12, 15],
        ["21:00", "00:00", "03:00", "06:00", "09:00", "12:00", "15:00"]
    )

    plt.tight_layout()
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.grid(True, color="#222222")

    path_to_savefile = os.path.join(
        PATH_TO_FIGURES, "sleep_history", "sleep_snake.png"
    )
    plt.savefig(path_to_savefile)
