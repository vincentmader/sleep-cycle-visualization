from datetime import datetime as dt
from datetime import timedelta as td
import os

import matplotlib.pyplot as plt

from config import MPL_THEME
from config import PATH_TO_FIGURES
from utils.file_io import load_sleepcycle_usage_from_file
from utils.cprint import cprint
from utils.timeseries import moving_avg


N = 50


def plot_sleep_cycle_usage():
    cprint(" Plotting SleepCycle usage...")

    timeseries = load_sleepcycle_usage_from_file()

    timestamps = sorted(timeseries.keys())
    sc_usage_bools = [timeseries[d] for d in timestamps]
    sc_usage_ints = [{True: 1, False: 0}[b] for b in sc_usage_bools]
    y = moving_avg(sc_usage_ints, N)
    dates = [dt.fromtimestamp(ts) for ts in timestamps]

    plt.style.use(MPL_THEME)

    fig = plt.figure(figsize=(10, 5))
    plt.title(f"SleepCycle usage - moving average over the last {N} days")
    plt.bar(dates, y,  color="orange", width=td(days=1))
    plt.xlim(dates[0], dates[-1])
    plt.ylim(0, 1)

    plt.tight_layout()
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    path_to_savefile = os.path.join(
        PATH_TO_FIGURES, "sleep_cycle", "usage.png"
    )
    plt.savefig(path_to_savefile)
