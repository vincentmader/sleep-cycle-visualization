from utils.cprint import cprint
from utils.timeseries import initialize_timeseries
from utils.file_io import load_nights_from_file
from utils.file_io import save_sleepcycle_usage_to_file


def get_usage():
    """Get a time-series dictionary encoding daily SleepCycle usage."""
    cprint(" Constructing SleepCycle usage time-series...")

    timeseries = initialize_timeseries(initial_value=False)

    nights = load_nights_from_file()
    for night in nights:
        date = night.date
        timeseries[date] = True

    save_sleepcycle_usage_to_file(timeseries)
    return timeseries
