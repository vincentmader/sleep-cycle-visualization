from .get_night_from_line_format_v1 import get_night_from_line_format_v1
from .get_night_from_line_format_v2 import get_night_from_line_format_v2


def get_night_from_line(line, export_type):
    split = line.split(';')
    if export_type == "v1":
        night = get_night_from_line_format_v1(split)
    elif export_type == "v2":
        night = get_night_from_line_format_v2(split)
    else:
        raise Exception(f"Export-type {export_type} is not defined")

    return night
