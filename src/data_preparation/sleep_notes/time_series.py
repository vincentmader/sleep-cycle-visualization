import numpy as np

from data_preparation.sleep_notes.names import translate_sleepnote
from utils.cprint import cprint
from utils.timeseries import initialize_timeseries_dict
from utils.file_io import load_translated_sleepnote_names_from_file
from utils.file_io import load_nights_from_file
from utils.file_io import save_sleepnote_timeseries_to_file
from utils.file_io import load_sleepnote_names_from_file
from utils.dates import get_all_dates
from utils.timeseries import TimeSeries


def construct_sleepnote_timeseries():
    """Create time-series for all sleep-notes.

    Returns:
        dict(str: dict(datetime.datetime: bool))

        Format: {
            sleepnote_name: {
                datetime: True/False/None,
                ...
            },
            ...
        }
    """
    cprint(" Constructing sleep-note time-series objects...")

    # Load list of all nights as `night.Night` object instances.
    nights = load_nights_from_file()
    # Load list of all sleep-note names.
    sleepnotes = load_sleepnote_names_from_file()

    # Prepare empty time-series.
    timeseries_dicts = {}
    for sn in sleepnotes:
        sn = translate_sleepnote(sn)
        if sn not in timeseries_dicts.keys():
            timeseries_dicts[sn] = initialize_timeseries_dict()

    # Loop over all nights, check whether each sleep-note was active.
    for night in nights:
        date = night.date
        for sn_1 in sleepnotes:
            sn_1 = translate_sleepnote(sn_1)
            found = False
            for sn_2 in night.sleep_notes:
                sn_2 = translate_sleepnote(sn_2)
                if sn_1 == sn_2:
                    found = True
            timeseries_dicts[sn_1][date] = found

    # Save time-series for each sleep-note to file.
    # dates = get_all_dates()
    translations = load_translated_sleepnote_names_from_file()
    for sleepnote in translations:
        dates = np.array(
            [i for i in sorted(timeseries_dicts[sleepnote].keys())]
        )
        values = np.array([
            timeseries_dicts[sleepnote][d] for d in dates
        ])
        timeseries = TimeSeries(dates, values)
        save_sleepnote_timeseries_to_file(
            timeseries, sleepnote
        )

    msg = f"   Constructed time-series object for {len(sleepnotes)} -> {len(translations)} sleep-notes."
    cprint(msg, "green")
    # return timeseries TODO
