import utils
from utils.cprint import cprint
from utils.timeseries import initialize_timeseries
from utils.file_io import load_translated_sleepnote_names_from_file
from data_preparation.sleep_notes.names import translate_sleepnote


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
    nights = utils.file_io.load_nights_from_file()
    # Load list of all sleep-note names.
    sleepnotes = utils.file_io.load_sleepnote_names_from_file()
    # Prepare empty time-series.
    timeseries = {}
    for sn in sleepnotes:
        sn = translate_sleepnote(sn)
        if sn not in timeseries.keys():
            timeseries[sn] = initialize_timeseries()

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
            timeseries[sn_1][date] = found

    # Save time-series for each sleep-note to file.
    translations = load_translated_sleepnote_names_from_file()
    for sleepnote in translations:
        utils.file_io.save_sleepnote_timeseries_to_file(
            timeseries[sleepnote], sleepnote
        )

    msg = f"   Constructed time-series object for {len(sleepnotes)} -> {len(translations)} sleep-notes."
    cprint(msg, "green")
    return timeseries
