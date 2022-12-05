from datetime import timedelta as td
import os

import numpy as np

from config import PATH_TO_DATA
from utils.cprint import cprint
from utils.file_io import load_from_pickle
from utils.file_io import save_to_pickle
from utils.timeseries import initialize_timeseries_dict
from utils.timeseries import TimeSeries


def get_sleep_history_timeseries():
    cprint(" Loading bed-times...")

    # Load "nights" dataset from file.
    path_to_savefile = os.path.join(PATH_TO_DATA, "out", "nights", "nights.p")
    nights = load_from_pickle(path_to_savefile)

    # Initialize timeseries dictionaries.
    timeseries_for_measurement_start = initialize_timeseries_dict()
    timeseries_for_measurement_end = initialize_timeseries_dict()
    timeseries_for_time_asleep_in_s = initialize_timeseries_dict()
    timeseries_for_time_before_sleep_in_s = initialize_timeseries_dict()
    timeseries_for_sleep_start = initialize_timeseries_dict()
    timeseries_for_sleep_end = initialize_timeseries_dict()
    timeseries_for_measurement_duration = initialize_timeseries_dict()
    timeseries_for_sleep_quality = initialize_timeseries_dict()
    timeseries_for_wakeup_mood = initialize_timeseries_dict()
    timeseries_for_heart_rate = initialize_timeseries_dict()
    timeseries_for_nr_of_steps = initialize_timeseries_dict()
    timeseries_for_sleep_regularity = initialize_timeseries_dict()
    timeseries_for_alarm_mode = initialize_timeseries_dict()
    timeseries_for_air_pressure_in_pa = initialize_timeseries_dict()
    timeseries_for_city_name = initialize_timeseries_dict()
    timeseries_for_nr_of_moves_per_hour = initialize_timeseries_dict()
    # window_start
    # window_end
    timeseries_for_did_snore = initialize_timeseries_dict()
    timeseries_for_snore_time = initialize_timeseries_dict()
    timeseries_for_weather_temp_in_c = initialize_timeseries_dict()
    timeseries_for_weather_type = initialize_timeseries_dict()

    # Load data into timeseries dictionaries.
    for night in nights:
        date = night.date

        measurement_start = night.measurement_start
        timeseries_for_measurement_start[date] = measurement_start

        measurement_end = night.measurement_end
        timeseries_for_measurement_end[date] = measurement_end

        time_before_sleep_in_s = night.time_before_sleep_in_s
        timeseries_for_time_before_sleep_in_s[date] = time_before_sleep_in_s

        time_asleep_in_s = night.time_asleep_in_s
        timeseries_for_time_asleep_in_s[date] = time_asleep_in_s

        if time_before_sleep_in_s != None:
            sleep_start = measurement_end + td(seconds=time_before_sleep_in_s)
        else:
            sleep_start = None
        timeseries_for_sleep_start[date] = sleep_start

        if sleep_start != None and time_asleep_in_s != None:
            sleep_end = sleep_start + td(seconds=time_asleep_in_s)
        else:
            sleep_end = None
        timeseries_for_sleep_end[date] = sleep_end

        timeseries_for_measurement_duration[date] = night.measurement_duration_in_s
        timeseries_for_sleep_quality[date] = night.sleep_quality
        timeseries_for_wakeup_mood[date] = night.wake_up_mood
        timeseries_for_heart_rate[date] = night.heart_rate
        timeseries_for_nr_of_steps[date] = night.nr_of_steps
        timeseries_for_sleep_regularity[date] = night.sleep_regularity
        timeseries_for_alarm_mode[date] = night.alarm_mode
        timeseries_for_air_pressure_in_pa[date] = night.air_pressure_in_pa
        timeseries_for_city_name[date] = night.city_name
        timeseries_for_nr_of_moves_per_hour[date] = night.nr_of_moves_per_h
        timeseries_for_did_snore[date] = night.did_snore
        timeseries_for_snore_time[date] = night.snore_time
        timeseries_for_weather_temp_in_c[date] = night.weather_temp_in_c
        timeseries_for_weather_type[date] = night.weather_type

    filenames_and_datasets = [
        ("measurement_start", timeseries_for_measurement_start),
        ("measurement_end", timeseries_for_measurement_end),
        ("time_before_sleep_in_s", timeseries_for_time_before_sleep_in_s),
        ("time_asleep_in_s", timeseries_for_time_asleep_in_s),
        ("sleep_start", timeseries_for_sleep_start),
        ("sleep_end", timeseries_for_sleep_end),
        ("measurement_duration_in_s", timeseries_for_measurement_duration),
        ("sleep_quality", timeseries_for_sleep_quality),
        ("wakeup_mood", timeseries_for_wakeup_mood),
        ("heart_rate", timeseries_for_heart_rate),
        ("nr_of_steps", timeseries_for_nr_of_steps),
        ("sleep_regularity", timeseries_for_sleep_regularity),
        ("alarm_mode", timeseries_for_alarm_mode),
        ("air_pressure_in_pa", timeseries_for_air_pressure_in_pa),
        ("city_name", timeseries_for_city_name),
        ("nr_of_moves_per_h", timeseries_for_nr_of_moves_per_hour),
        ("did_snore", timeseries_for_did_snore),
        ("snore_time", timeseries_for_snore_time),
        ("weather_temp_in_c", timeseries_for_weather_temp_in_c),
        ("weather_type", timeseries_for_weather_type),
    ]

    # Save to file.
    path_to_savefiles = os.path.join(PATH_TO_DATA, "out", "sleep_history")
    for filename, dataset in filenames_and_datasets:
        dates = np.array(sorted([d for d in dataset.keys()]))
        values = np.array([dataset[d] for d in dates])
        dataset = TimeSeries(dates, values)
        path_to_savefile = os.path.join(path_to_savefiles, f"{filename}.p")
        save_to_pickle(dataset, path_to_savefile)

    return filenames_and_datasets
