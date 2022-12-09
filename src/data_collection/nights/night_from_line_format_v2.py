from datetime import datetime as dt

from night import Night
from utils import get_date_from_str


def get_night_from_line_format_v2(split):
    measurement_start = get_date_from_str(split[0])
    measurement_end = get_date_from_str(split[1])
    date = dt(
        measurement_start.year, measurement_start.month, measurement_start.day
    )
    sleep_quality = float(split[2][:-1]) / 100
    sleep_regularity = float(split[3][:-1]) / 100
    wake_up_mood = {"": None, "Good": 1, "OK": 0, "Bad": -1}[split[4]]
    heart_rate = None if split[5] in ["", "0"] else float(split[5])
    nr_of_steps = None if split[6] == "" else float(split[6])
    alarm_mode = split[7]
    air_pressure_in_pa = None if split[8] == "" else float(split[8])
    city_name = None if split[9] == "" else split[9]
    nr_of_moves_per_h = None if split[10] in ["", "0"] else float(split[10])
    measurement_duration_in_h = None if split[11] == "" else float(split[11])/3600
    time_asleep_in_h = None if split[11] == "" else float(split[12])/3600
    time_before_sleep_in_h = None if split[13] == "" else float(split[13])/3600
    window_start = None if split[14] == "" else get_date_from_str(split[14])
    window_end = None if split[15] == "" else get_date_from_str(split[15])
    did_snore = {"false": False, "true": True}[split[16]]
    snore_time = None if split[17] == "" else float(split[17])
    weather_temp_in_c = None if split[18] == "" else float(split[18])
    weather_type = None if split[19] == "" else split[19]
    sleep_notes = [] if split[20] == "\n" else split[20][:-1].split(":")

    return Night(
        date,
        measurement_start,
        measurement_end,
        measurement_duration_in_h,
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
        time_asleep_in_h=time_asleep_in_h,
        time_before_sleep_in_h=time_before_sleep_in_h,
        window_start=window_start,
        window_end=window_end,
        did_snore=did_snore,
        snore_time=snore_time,
        weather_temp_in_c=weather_temp_in_c,
        weather_type=weather_type,
    )
