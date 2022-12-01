#!/usr/bin/env python3
import data_collection
import data_preparation
import data_visualization


if __name__ == "__main__":
    data_collection.nights.all_nights.get_all_nights()

    data_preparation.sleep_cycle.usage.get_usage()
    data_preparation.sleep_notes.names.get_sleepnote_names()
    data_preparation.sleep_notes.names.get_translated_sleepnote_names()
    data_preparation.sleep_notes.time_series.construct_sleepnote_timeseries_objects()

    data_visualization.sleep_cycle.usage.plot_sleep_cycle_usage()
    data_visualization.sleep_notes.moving_average.plot_moving_average()

    # DONE 1. save complete sleep history to file
    # DONE 2. load complete sleep history from file
    # TODO 3. visualize sleep history
    # TODO 3.a) plot sleep-snake
    # TODO 3.b) plot "frequency" of sleep notes
    # TODO 3.b) plot histograms of bed-time, wake-up-time, time-in-bed, ...
    # TODO 3...
