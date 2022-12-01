from tqdm import tqdm

from utils.cprint import cprint
from utils.dates import prepare_empty_timeseries
from utils.file_io import load_nights_from_file
from utils.file_io import save_sleepcycle_usage_to_file


def get_usage():
    """Get a time-series dictionary encoding daily SleepCycle usage."""
    cprint("\n Constructing SleepCycle usage time-series...")

    timeseries = prepare_empty_timeseries(initial_value=False)

    nights = load_nights_from_file()
    for night in tqdm(nights):
        date = night.date
        timeseries[date.timestamp()] = True

    save_sleepcycle_usage_to_file(timeseries)
    return timeseries
