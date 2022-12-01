import os

from tqdm import tqdm

from config import PATH_TO_FIGURES
from utils.cprint import cprint
from utils.file_io import load_nights_from_file
from utils.dates import prepare_empty_timeseries
from utils.file_io import save_to_pickle


def get_sleep_quality_over_time():
    cprint(" Loading sleep-quality...")

    timeseries = prepare_empty_timeseries()

    nights = load_nights_from_file()
    for night in nights:
        date = night.date
        sleep_quality = night.sleep_quality
        timeseries[date] = sleep_quality

    path_to_savefile = os.path.join(
        PATH_TO_FIGURES, "sleep_history", "sleep_quality.p"
    )
    save_to_pickle(timeseries, path_to_savefile)
