from datetime import timedelta as td
import os

import matplotlib.pyplot as plt

from config import MPL_THEME
from config import PATH_TO_FIGURES
from utils.file_io import load_sleepcycle_usage_from_file
from utils.cprint import cprint
from utils.timeseries import moving_avg


# Define moving-average window-size.
N = 50


def plot_sleep_cycle_usage():
    cprint(" Plotting SleepCycle usage...")

    # Load time-series data for sleep-cycle usage.
    timeseries = load_sleepcycle_usage_from_file()
    dates = timeseries.dates
    sc_usage_bools = timeseries.values
    # Convert boolean usage time-series to integers.
    sc_usage_ints = [{True: 1, False: 0}[b] for b in sc_usage_bools]
    # Create moving-average for sleep-cycle usage.
    y = moving_avg(sc_usage_ints, N)

    # Apply style to plot.
    plt.style.use(MPL_THEME)
    # Create figure.
    plt.figure(figsize=(10, 5))

    # Plot usage time-series.
    plt.bar(dates, y,  color="orange", width=td(days=1))

    # Configure plot.
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.title(f"SleepCycle usage - moving average over the last {N} days")
    plt.xlim(dates[0], dates[-1])
    plt.ylim(0, 1)
    plt.tight_layout()

    # Save to file.
    path_to_savefile = os.path.join(
        PATH_TO_FIGURES, "sleep_cycle", "usage.png"
    )
    plt.savefig(path_to_savefile)
    plt.close()
