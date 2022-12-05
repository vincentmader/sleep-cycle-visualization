import os

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

from config import MPL_THEME
from config import PATH_TO_FIGURES
from utils.cprint import cprint
from utils.file_io import load_sleepnote_timeseries_from_file
from utils.file_io import load_translated_sleepnote_names_from_file
from utils.timeseries import TimeSeries


# Define moving-average window-size.
N = 50
# Define path to figures directory.
PATH_TO_FIGURES = os.path.join(PATH_TO_FIGURES, "sleep_notes")


def plot_moving_average():
    cprint(" Plotting sleep-note moving-averages...")

    # Setup plot.
    plt.style.use(MPL_THEME)
    fig = plt.figure(figsize=(10, 5))

    # Load names of all sleep-notes.
    sleepnote_names = load_translated_sleepnote_names_from_file()
    for sleepnote in tqdm(sorted(sleepnote_names)):
        # Load timeseries data for sleep-note usage.
        sn_usage_timeseries = load_sleepnote_timeseries_from_file(sleepnote)
        dates = sn_usage_timeseries.dates
        values = sn_usage_timeseries.values
        # Convert boolean usage time-series to integers.
        values = np.array([ {True: 1, False: 0, None: 0}[b] for b in values])
        sn_usage_ints = TimeSeries(dates, values)
        # Calculate moving-average for sleep-note usage.
        sn_usage_mavg = sn_usage_ints.moving_average(N)

        # Plot moving-average sleep-note usage.
        plt.plot(dates, sn_usage_mavg, color="orange")

        # Configure plot.
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.title(f"{sleepnote} - moving average over the last {N} days")
        plt.xlim(dates[0], dates[-1])
        plt.ylim(0, 1)
        plt.tight_layout()

        # Save to file & clear plot.
        filename = f"{sleepnote}.png"
        path_to_savefile = os.path.join(PATH_TO_FIGURES, filename)
        plt.savefig(path_to_savefile)
        fig.clear()
