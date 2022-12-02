from utils.cprint import cprint
from utils.file_io import load_nights_from_file
from utils.file_io import save_sleepcycle_usage_to_file
from utils.timeseries import TimeSeries
from utils.dates import get_all_dates


def get_usage():
    """Get a time-series dictionary encoding daily SleepCycle usage."""
    cprint(" Constructing time-series for sleep-cycle usage...")

    nights = load_nights_from_file()

    ts = {date: False for date in get_all_dates()}
    for night in nights:
        ts[night.date] = True
    dates = sorted(ts.keys())
    values = [ts[d] for d in dates]
    timeseries = TimeSeries(dates, values)

    save_sleepcycle_usage_to_file(timeseries)

    return timeseries
