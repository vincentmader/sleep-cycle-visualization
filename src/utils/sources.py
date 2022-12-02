import os

from config import PATH_TO_SC_EXPORTS


def get_export_type_from_filepath(filepath):
    # Get filename from filepath.
    filename = os.path.split(filepath)[1]

    # Get export-type from filename.
    if "5" in filename:
        export_type = "v1"
    elif "6S" in filename:
        export_type = "v2"
    else:
        raise Exception(f"Export-type for file {filename} is not defined")

    return export_type


def get_paths_to_sleepcycle_export_files():
    # Load list of all csv-export filenames.
    filenames = os.listdir(PATH_TO_SC_EXPORTS)
    filenames = [f for f in filenames if f.endswith(".csv")]

    # Load list of all csv-export filepaths.
    filepaths = [os.path.join(PATH_TO_SC_EXPORTS, f) for f in filenames]

    return filepaths
