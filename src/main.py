#!/usr/bin/env python3
from data_preparation.rename_note import rename_note
import data_collection
import data_preparation
import os

import matplotlib.pyplot as plt
from tqdm import tqdm

from config import PATH_TO_FIGURES
from utils.cprint import cprint


def create_moving_avg_plot(note_name, note_history):
    x = note_history.keys()
    y = note_history.values()

    plt.plot(x, y)

    dirname = "Sleep-Note Usage vs. Time (moving avg.)"
    filename = f"{note_name}.png"
    path_to_file = os.path.join(PATH_TO_FIGURES, dirname, filename)
    plt.savefig(path_to_file)
    plt.close()


if __name__ == "__main__":
    nights = data_collection.get_nights()

    # TODO 1. save complete sleep history to file
    # TODO 2. load complete sleep history from file
    # TODO 3. visualize sleep history
    # TODO 3.a) plot sleep-snake
    # TODO 3.b) plot "frequency" of sleep notes
    # TODO 3.b) plot histograms of bed-time, wake-up-time, time-in-bed, ...
    # TODO 3...

    _, notes = data_preparation.prepare_sleep_note_time_series(nights)

    for night in nights:
        date = night.date
        # Initialize all notes to false, on days where sleep was tracked.
        for note in notes:
            notes[note][date] = False
        # If sleep note was active for that day, then set to true
        notes_for_night = night.sleep_notes
        for note in notes_for_night:
            note = rename_note(note)
            notes[note][date] = True

    cprint("\n Creating plots...")
    for note_name in tqdm(notes):
        create_moving_avg_plot(note_name, notes[note_name])

    # print(notes)
