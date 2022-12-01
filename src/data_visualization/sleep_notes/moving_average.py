from datetime import datetime as dt
import os

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

from config import PATH_TO_FIGURES
from utils.cprint import cprint
from utils.file_io import load_sleepnote_timeseries_from_file
from utils.file_io import load_translated_sleepnote_names_from_file


N = 50


def nr_of_logged_nights(timeseries):
    y = []
    for i, _ in enumerate(timeseries):
        y_i = 0
        for j in range(min(i+1, N)):
            boolean = timeseries[i - j]
            if boolean in [True, False]:
                y_i += 1
        y.append(y_i)
    return y


def moving_avg(arr):
    y = []
    for i, _ in enumerate(arr):
        nr_of_logged_notes = None
        nr_of_logged_nights = 0
        for j in range(min(i, N)):
            boolean = arr[i - j]
            if boolean in (True, False):
                nr_of_logged_nights += 1
                if nr_of_logged_notes == None:
                    nr_of_logged_notes = 0
                if boolean == True:
                    nr_of_logged_notes += 1

        if nr_of_logged_notes:
            nr_of_logged_notes /= nr_of_logged_nights
        y.append(nr_of_logged_notes)
    return y


def plot_moving_average():
    cprint("\n Plotting sleep-note moving-averages...")

    mpl_theme = "~/.config/matplotlib/dark.mplstyle"
    plt.style.use(mpl_theme)

    sleepnote_names = load_translated_sleepnote_names_from_file()
    for sleepnote in tqdm(sorted(sleepnote_names)):
        timeseries = load_sleepnote_timeseries_from_file(sleepnote)

        timestamps = sorted(timeseries.keys())
        booleans = [timeseries[i] for i in timestamps]

        dates = [dt.fromtimestamp(i) for i in timestamps]
        y = moving_avg(booleans)

        # fig = plt.figure(figsize=(10, 5))
        # y = nr_of_logged_nights(booleans)
        # plt.plot(dates, y)
        # plt.show()

        # a = {None: -1, False: 0, True: 1}
        # y = [a[i] for i in booleans]
        # y = np.array(y)
        # plt.plot(dates, y)
        # plt.show()

        fig = plt.figure(figsize=(10, 5))
        # plt.title(f"{sleepnote}        (m.avg. with {N=})")
        plt.title(f"{sleepnote}")
        # plt.plot(dates, y, color="green")
        plt.plot(dates, y, color="green")
        # plt.scatter(dates, y, s=0.5)
        plt.xlim(dates[0], dates[-1])
        plt.ylim(0, 1)
        plt.tight_layout()

        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        # ax.spines['left'].set_visible(False)
        # ax.get_yaxis().set_ticks([])

        filename = f"{sleepnote}.png"
        path_to_figures = os.path.join(PATH_TO_FIGURES, "sleep_notes")
        path_to_savefile = os.path.join(path_to_figures, filename)
        plt.savefig(path_to_savefile)
        plt.close()
