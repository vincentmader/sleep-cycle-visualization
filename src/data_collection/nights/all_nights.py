from .night_from_line import get_night_from_line
from utils.cprint import cprint
from utils.file_io import load_file_to_line_list
from utils.file_io import save_nights_to_file
from utils.sources import get_export_type_from_filepath
from utils.sources import get_paths_to_sleepcycle_export_files


def get_all_nights():
    cprint(" Loading nights from sleep-history exports...")

    # Load filepaths of all export-files.
    export_filepaths = get_paths_to_sleepcycle_export_files()

    # Create list of night objects.
    nights = []
    for filepath in export_filepaths:
        export_type = get_export_type_from_filepath(filepath)
        lines = load_file_to_line_list(filepath)
        for line in lines[1:]:
            night = get_night_from_line(line, export_type)
            nights.append(night)

    # Save list of nights to file.
    save_nights_to_file(nights)
    
    # Print information.
    year_min, year_max = nights[0].date.year, nights[-1].date.year
    msg = f"   Loaded {len(nights)} nights from {year_min} to {year_max}."
    cprint(msg, "green")
    return nights
