#!/usr/bin/env python3
import data_collection
import data_preparation
import data_processing
import data_visualization

# DONE 1. save complete sleep history to file
# DONE 2. load complete sleep history from file
# DONE 3. visualize sleep history
# DONE 3.a) plot sleep-snake
# DONE 3.b) plot "frequency" of sleep notes
# TODO 3.b) plot histograms of bed-time, wake-up-time, time-in-bed, ...


def collect():
    print()
    data_collection.nights.all_nights.get_all_nights()


def prepare():
    print()
    data_preparation.sleep_cycle.usage.get_usage()
    data_preparation.sleep_notes.names.get_sleepnote_names()
    data_preparation.sleep_notes.names.get_translated_sleepnote_names()
    data_preparation.sleep_notes.time_series.construct_sleepnote_timeseries()
    data_preparation.sleep_history.timeseries.get_sleep_history_timeseries()


def process():
    pass


def visualize():
    print()
    data_visualization.sleep_history.sleep_snake.plot_sleep_snake()
    data_visualization.sleep_cycle.usage.plot_sleep_cycle_usage()
    data_visualization.sleep_history.histograms.plot_histograms()
    data_visualization.sleep_notes.usage.plot_moving_average()


if __name__ == "__main__":
    collect()
    prepare()
    # process()
    visualize()
