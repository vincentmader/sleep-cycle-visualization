from datetime import datetime as dt
from datetime import timedelta as td

import data_preparation
from config import START_DATE


def prepare_sleep_note_time_series(nights):
    # Define time axis.
    n = (dt.now() - START_DATE).days
    time = [START_DATE + td(days=i) for i in range(n)]

    # Get names of all sleep notes.
    note_names = data_preparation.get_list_of_sleep_note_names(nights)

    # Define notes axis.
    notes = {}
    for note_name in note_names:
        # Rename note.
        note_name = data_preparation.rename_note(note_name)
        # Initialize None for all sleep-notes & at all times.
        if note_name not in notes:
            notes[note_name] = {}
        for t in time:
            notes[note_name][t] = None

    return time, notes
