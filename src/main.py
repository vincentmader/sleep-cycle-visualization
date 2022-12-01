#!/usr/bin/env python3
from data_preparation.rename_note import rename_note
import data_collection
import data_preparation
import data_visualization


if __name__ == "__main__":
    data_collection.nights.all_nights.get_all_nights()
    data_preparation.sleep_notes.names.get_sleepnote_names()
    data_preparation.sleep_notes.names.get_translated_sleepnote_names()
    data_preparation.sleep_notes.time_series.construct_sleepnote_timeseries_objects()
    data_visualization.sleep_notes.moving_average.plot_moving_average()

    # DONE 1. save complete sleep history to file
    # DONE 2. load complete sleep history from file
    # TODO 3. visualize sleep history
    # TODO 3.a) plot sleep-snake
    # TODO 3.b) plot "frequency" of sleep notes
    # TODO 3.b) plot histograms of bed-time, wake-up-time, time-in-bed, ...
    # TODO 3...

    # _, notes = data_preparation.prepare_sleep_note_time_series(nights)

    # for night in nights:
    #     date = night.date
    #     # Initialize all notes to false, on days where sleep was tracked.
    #     for note in notes:
    #         notes[note][date] = False
    #     # If sleep note was active for that day, then set to true
    #     notes_for_night = night.sleep_notes
    #     for note in notes_for_night:
    #         note = rename_note(note)
    #         notes[note][date] = True

    # cprint("\n Creating plots...")
    # for note_name in tqdm(notes):
    #     create_moving_avg_plot(note_name, notes[note_name])


# def create_moving_avg_plot(note_name, note_history):
    # x = note_history.keys()
    # y = note_history.values()

    # plt.plot(x, y)

    # dirname = "Sleep-Note Usage vs. Time (moving avg.)"
    # filename = f"{note_name}.png"
    # path_to_file = os.path.join(PATH_TO_FIGURES, dirname, filename)
    # plt.savefig(path_to_file)
    # plt.close()
