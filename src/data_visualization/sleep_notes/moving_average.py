from datetime import datetime as dt
from datetime import timedelta as td
import os

import matplotlib.pyplot as plt
from tqdm import tqdm

from config import MPL_THEME
from config import PATH_TO_FIGURES
from utils.cprint import cprint
from utils.file_io import load_sleepnote_timeseries_from_file
from utils.file_io import load_translated_sleepnote_names_from_file
from utils.file_io import load_sleepcycle_usage_from_file
from utils.timeseries import moving_avg


N = 50


def plot_moving_average():
    cprint(" Plotting sleep-note moving-averages...")

    plt.style.use(MPL_THEME)
    fig = plt.figure(figsize=(10, 5))

    sc_usage_timeseries = load_sleepcycle_usage_from_file()
    dates = sorted(sc_usage_timeseries.keys())
    sc_usage_bools = [sc_usage_timeseries[i] for i in dates]
    sc_usage_ints = [
        {True: 1, False: 0, None: 0}[b] for b in sc_usage_bools
    ]
    sc_usage_mavg = moving_avg(sc_usage_ints, N)

    sleepnote_names = load_translated_sleepnote_names_from_file()
    for sleepnote in tqdm(sorted(sleepnote_names)):
        sn_usage_timeseries = load_sleepnote_timeseries_from_file(sleepnote)

        sn_usage_bools = [sn_usage_timeseries[i] for i in dates]
        sn_usage_ints = [
            {True: 1, False: 0, None: 0}[b] for b in sn_usage_bools
        ]
        sn_usage_mavg = moving_avg(sn_usage_ints, N)
        sn_usage_mavg *= sc_usage_mavg

        plt.title(f"{sleepnote} - moving average over the last {N} days")
        plt.plot(dates, sn_usage_mavg, color="orange")
        # plt.bar(dates, y,  color="orange", width=td(days=1))
        # plt.xlim(dates[0], dates[-1])
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
        fig.clear()
