#!/usr/bin/env python3
from datetime import datetime as dt
import os

from tqdm import tqdm

from night import Night

PATH_TO_SC_EXPORTS = './data/exports'


def load_file_to_list_of_lines(filepath):
    print(f"\nLoading {filename}...")
    with open(filepath, "r") as fp:
        lines = fp.readlines()
    return lines


def get_date_from_str(string):
    return dt.strptime(string, "%Y-%m-%d %H:%M:%S")


def get_sleep_history_from_lines(lines, export_type):
    sleep_history = []
    for line in tqdm(lines[1:]):
        night = get_night_from_line(line, export_type)
        sleep_history.append(night)
    return sleep_history


def get_night_from_line(line, export_type):
    split = line.split(';')
    if export_type == "old":
        night = get_night_from_old_format(split)
    elif export_type == "new":
        night = get_night_from_new_format(split)
    else:
        raise Exception(f"Export-type {export_type} is not defined")
    return night


def get_night_from_old_format(split):
    measurement_start = get_date_from_str(split[0])
    measurement_end = get_date_from_str(split[1])
    sleep_quality = float(split[2][:-1]) / 100
    tmp = split[3].split(":")
    measurement_duration_in_s = (float(tmp[0])*60 + float(tmp[1])) * 60
    wake_up_mood = {"": None, ":)": 1, ":|": 0, ":(": -1}[split[4]]
    sleep_notes = [] if split[5] == "" else split[5].split(":")
    heart_rate = None if split[6] == "" else float(split[6])
    nr_of_steps = None if split[7] == "" else float(split[7])

    return Night(
        measurement_start,
        measurement_end,
        measurement_duration_in_s,
        sleep_quality,
        sleep_notes,
        wake_up_mood,
        heart_rate,
        nr_of_steps
    )


def get_night_from_new_format(split):
    measurement_start = get_date_from_str(split[0])
    measurement_end = get_date_from_str(split[1])
    sleep_quality = float(split[2][:-1]) / 100
    sleep_regularity = float(split[3][:-1]) / 100
    wake_up_mood = {"": None, "Good": 1, "OK": 0, "Bad": -1}[split[4]]
    heart_rate = None if split[5] in ["", "0"] else float(split[5])
    nr_of_steps = None if split[6] == "" else float(split[6])
    alarm_mode = split[7]
    air_pressure_in_pa = None if split[8] == "" else float(split[8])
    city_name = None if split[9] == "" else split[9]
    nr_of_moves_per_h = None if split[10] in ["", "0"] else float(split[10])
    measurement_duration_in_s = None if split[11] == "" else float(split[11])
    time_asleep_in_s = None if split[11] == "" else float(split[12])
    time_before_sleep_in_s = None if split[13] == "" else float(split[13])
    window_start = None if split[14] == "" else get_date_from_str(split[14])
    window_end = None if split[15] == "" else get_date_from_str(split[15])
    did_snore = {"false": False, "true": True}[split[16]]
    snore_time = None if split[17] == "" else float(split[17])
    weather_temp_in_c = None if split[18] == "" else float(split[18])
    weather_type = None if split[19] == "" else split[19]
    sleep_notes = [] if split[20] == "" else split[20].split(":")

    return Night(
        measurement_start,
        measurement_end,
        measurement_duration_in_s,
        sleep_quality,
        sleep_notes,
        wake_up_mood,
        heart_rate,
        nr_of_steps,
        sleep_regularity=sleep_regularity,
        alarm_mode=alarm_mode,
        air_pressure_in_pa=air_pressure_in_pa,
        city_name=city_name,
        nr_of_moves_per_h=nr_of_moves_per_h,
        time_asleep_in_s=time_asleep_in_s,
        time_before_sleep_in_s=time_before_sleep_in_s,
        window_start=window_start,
        window_end=window_end,
        did_snore=did_snore,
        snore_time=snore_time,
        weather_temp_in_c=weather_temp_in_c,
        weather_type=weather_type,
    )


if __name__ == "__main__":
    sleep_history = []
    for filename in os.listdir(PATH_TO_SC_EXPORTS):
        if not filename.endswith(".csv"):
            continue
        export_type = "old" if "5" in filename else "new"
        filepath = os.path.join(PATH_TO_SC_EXPORTS, filename)
        lines = load_file_to_list_of_lines(filepath)
        file_sleep_history = get_sleep_history_from_lines(lines, export_type)
        for entry in file_sleep_history:
            sleep_history.append(entry)

    print(f"\nSuccessfully loaded {len(sleep_history)} nights.")

    # TODO 1. save complete sleep history to file
    # TODO 2. load complete sleep history from file
    # TODO 3. visualize sleep history
    # TODO 3.a) plot sleep-snake
    # TODO 3.b) plot "frequency" of sleep notes
    # TODO 3.b) plot histograms of bed-time, wake-up-time, time-in-bed, ...
    # TODO 3...
