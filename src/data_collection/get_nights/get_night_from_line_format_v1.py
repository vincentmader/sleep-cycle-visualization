from datetime import datetime as dt

from night import Night
import utils


def get_night_from_line_format_v1(split):
    measurement_start = utils.dates.get_date_from_str(split[0])
    measurement_end = utils.dates.get_date_from_str(split[1])
    date = dt(
        measurement_start.year, measurement_start.month, measurement_start.day
    )
    sleep_quality = float(split[2][:-1]) / 100
    tmp = split[3].split(":")
    measurement_duration_in_s = (float(tmp[0])*60 + float(tmp[1])) * 60
    wake_up_mood = {"": None, ":)": 1, ":|": 0, ":(": -1}[split[4]]
    sleep_notes = [] if split[5] == "" else split[5].split(":")
    heart_rate = None if split[6] == "" else float(split[6])
    nr_of_steps = None if split[7] == "" else float(split[7])

    return Night(
        date,
        measurement_start,
        measurement_end,
        measurement_duration_in_s,
        sleep_quality,
        sleep_notes,
        wake_up_mood,
        heart_rate,
        nr_of_steps
    )
