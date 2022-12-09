from datetime import timedelta as td
import os

import matplotlib.pyplot as plt
import numpy as np

from config import MPL_THEME
from config import PATH_TO_FIGURES
from config import PATH_TO_DATA_OUT
from utils.cprint import cprint
from utils.file_io import load_from_pickle
from utils.dates import get_all_dates
from utils.timeseries import TimeSeries

# Define path to save-file directory for sleep-history datasets.
PATH_TO_SAVEFILES = os.path.join(PATH_TO_DATA_OUT, "sleep_history")
# Define moving-average window-size.
N = 50


def reformat_timeseries_data(
    all_dates,
    timeseries_for_measurement_start,
    timeseries_for_measurement_end,
    timeseries_for_measurement_duration_in_h
):
    # Initialize return values.
    dates = np.array([])
    starts_in_h = np.array([])
    ends_in_h = np.array([])
    durations_in_h = np.array([])

    starts = timeseries_for_measurement_start.values
    ends = timeseries_for_measurement_end.values
    durations = timeseries_for_measurement_duration_in_h.values

    for date, start, end, duration in zip(all_dates, starts, ends, durations):
        if start == None or duration == None or end == None:
            continue

        start = start.hour\
            + start.minute / 60\
            + start.second / 3600
        duration = duration
        end = end.hour\
            + end.minute / 60\
            + end.second / 3600

        if start > 15:
            start -= 24
        # if end > 18:
        #     end -= 24

        dates = np.append(dates, date)
        starts_in_h = np.append(starts_in_h, start)
        ends_in_h = np.append(ends_in_h, end)
        durations_in_h = np.append(durations_in_h, duration)

    return dates, starts_in_h, ends_in_h, durations_in_h


def plot_sleep_snake():
    cprint(" Plotting sleep-snake...")

    all_dates = get_all_dates()

    # Load timeseries data for measurement-start.
    filename = "measurement_start.p"
    path_to_savefile = os.path.join(PATH_TO_SAVEFILES, filename)
    measurement_starts = load_from_pickle(path_to_savefile)
    # Load timeseries data for measurement-end.
    filename = "measurement_end.p"
    path_to_savefile = os.path.join(PATH_TO_SAVEFILES, filename)
    measurement_ends = load_from_pickle(path_to_savefile)
    # Load timeseries data for measurement-duration (in seconds).
    filename = "measurement_duration_in_h.p"
    path_to_savefile = os.path.join(PATH_TO_SAVEFILES, filename)
    measurement_durations_in_h = load_from_pickle(path_to_savefile)

    res = reformat_timeseries_data(
        all_dates,
        measurement_starts,
        measurement_ends,
        measurement_durations_in_h
    )
    dates, starts_in_h, ends_in_h, durations_in_h = res

    # Create figure.
    plt.style.use(MPL_THEME)
    plt.figure(figsize=(16, 6))

    plt.bar(
        dates,
        durations_in_h,
        bottom=starts_in_h,
        width=td(days=1),
        color="gray"
    )
    starts_in_h = TimeSeries(dates, starts_in_h)
    starts_in_h = starts_in_h.moving_average(N)
    ends_in_h = TimeSeries(dates, ends_in_h)
    ends_in_h = ends_in_h.moving_average(N)

    plt.plot(dates, starts_in_h.values, "green")
    plt.plot(dates, ends_in_h.values, "red")

    # Configure plot.
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    plt.xlim(dates[0], dates[-1])
    plt.ylim(-3, 18)  # ?
    plt.yticks(
        [-3, 0, 3, 6, 9, 12, 15],
        ["21:00", "00:00", "03:00", "06:00", "09:00", "12:00", "15:00"]
    )
    plt.tight_layout()
    plt.grid(True, color="#222222")

    # Save to file.
    path_to_savefile = os.path.join(
        PATH_TO_FIGURES, "sleep_history", "sleep_snake.png"
    )
    plt.savefig(path_to_savefile)
    plt.close()
