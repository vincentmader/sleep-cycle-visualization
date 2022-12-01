from datetime import timedelta as td
import os

import numpy as np

from config import PATH_TO_DATA
from utils.cprint import cprint
from utils.file_io import load_from_pickle
from utils.file_io import save_to_pickle
from utils.dates import prepare_empty_timeseries

def get_sleep_history_timeseries():
    cprint(" Loading bed-times...")

    path_to_savefile = os.path.join(PATH_TO_DATA, "out", "nights", "nights.p")
    nights = load_from_pickle(path_to_savefile)

    list_measurement_start = prepare_empty_timeseries()
    list_measurement_end = prepare_empty_timeseries()
    list_time_asleep_in_s = prepare_empty_timeseries()
    list_time_before_sleep_in_s = prepare_empty_timeseries()
    list_sleep_start = prepare_empty_timeseries()
    list_sleep_end = prepare_empty_timeseries()
    list_measurement_duration = prepare_empty_timeseries()
    list_sleep_quality = prepare_empty_timeseries()
    list_wakeup_mood = prepare_empty_timeseries()
    list_heart_rate = prepare_empty_timeseries()
    list_nr_of_steps = prepare_empty_timeseries()
    list_sleep_regularity = prepare_empty_timeseries()
    list_alarm_mode = prepare_empty_timeseries()
    list_air_pressure_in_pa = prepare_empty_timeseries()
    list_city_name = prepare_empty_timeseries()
    list_nr_of_moves_per_hour = prepare_empty_timeseries()
    # window_start
    # window_end
    list_did_snore = prepare_empty_timeseries()
    list_snore_time = prepare_empty_timeseries()
    list_weather_temp_in_c = prepare_empty_timeseries()
    list_weather_type = prepare_empty_timeseries()

    for night in nights:
        date = night.date

        measurement_start = night.measurement_start
        list_measurement_start[date] = measurement_start

        measurement_end = night.measurement_end
        list_measurement_end[date] = measurement_end

        time_before_sleep_in_s = night.time_before_sleep_in_s
        list_time_before_sleep_in_s[date] = time_before_sleep_in_s

        time_asleep_in_s = night.time_asleep_in_s
        list_time_asleep_in_s[date] = time_asleep_in_s

        if time_before_sleep_in_s != None:
            sleep_start = measurement_end + td(seconds=time_before_sleep_in_s)
        else:
            sleep_start = None
        list_sleep_start[date] = sleep_start

        if sleep_start != None and time_asleep_in_s != None:
            sleep_end = sleep_start + td(seconds=time_asleep_in_s)
        else:
            sleep_end = None
        list_sleep_end[date] = sleep_end

        list_measurement_duration[date] = night.measurement_duration_in_s
        list_sleep_quality[date] = night.sleep_quality
        list_wakeup_mood[date] = night.wake_up_mood
        list_heart_rate[date] = night.heart_rate
        list_nr_of_steps[date] = night.nr_of_steps
        list_sleep_regularity[date] = night.sleep_regularity
        list_alarm_mode[date] = night.alarm_mode
        list_air_pressure_in_pa[date] = night.air_pressure_in_pa
        list_city_name[date] = night.city_name
        list_nr_of_moves_per_hour[date] = night.nr_of_moves_per_h
        list_did_snore[date] = night.did_snore
        list_snore_time[date] = night.snore_time
        list_weather_temp_in_c[date] = night.weather_temp_in_c
        list_weather_type[date] = night.weather_type

    filenames_and_datasets = [
        ("measurement_start", list_measurement_start),
        ("measurement_end", list_measurement_end),
        ("time_before_sleep_in_s", list_time_before_sleep_in_s),
        ("time_asleep_in_s", list_time_asleep_in_s),
        ("sleep_start", list_sleep_start),
        ("sleep_end", list_sleep_end),
        ("measurement_duration_in_s", list_measurement_duration),
        ("sleep_quality", list_sleep_quality),
        ("wakeup_mood", list_wakeup_mood),
        ("heart_rate", list_heart_rate),
        ("nr_of_steps", list_nr_of_steps),
        ("sleep_regularity", list_sleep_regularity),
        ("alarm_mode", list_alarm_mode),
        ("air_pressure_in_pa", list_air_pressure_in_pa),
        ("city_name", list_city_name),
        ("nr_of_moves_per_h", list_nr_of_moves_per_hour),
        ("did_snore", list_did_snore),
        ("snore_time", list_snore_time),
        ("weather_temp_in_c", list_weather_temp_in_c),
        ("weather_type", list_weather_type),
    ]

    path_to_savefiles = os.path.join(PATH_TO_DATA, "out", "sleep_history")
    for filename, dataset in filenames_and_datasets:
        path_to_savefile = os.path.join(path_to_savefiles, f"{filename}.p")
        save_to_pickle(dataset, path_to_savefile) 
    return filenames_and_datasets
