import os

from config import PATH_TO_SC_EXPORTS
import utils
from utils import cprint
from .get_night_from_line import get_night_from_line


def get_nights():
    nights = []

    filenames = os.listdir(PATH_TO_SC_EXPORTS)
    filenames = [f for f in filenames if f.endswith(".csv")]

    cprint("\n Loading nights from sleep-history exports...")
    for filename in filenames:
        export_type = "v1" if "5" in filename else "v2"

        filepath = os.path.join(PATH_TO_SC_EXPORTS, filename)
        lines = utils.load_file_to_line_list(filepath)

        for line in lines[1:]:
            night = get_night_from_line(line, export_type)
            nights.append(night)

    utils.file_io.save_nights_to_file(nights)

    year_min, year_max = nights[0].date.year, nights[-1].date.year
    cprint(f" SUCCESS: Loaded {len(nights)} nights from {year_min} to {year_max} into memory.", "green")
    return nights
