import json
import os
import pickle

import config
from config import PATH_TO_DATA_OUT


def load_file_to_line_list(filepath):
    with open(filepath, "r") as fp:
        lines = fp.readlines()
    return lines


def load_from_pickle(path_to_savefile):
    with open(path_to_savefile, 'rb') as fp:
        data = pickle.load(fp)
    return data


def save_to_pickle(data, path_to_savefile):
    with open(path_to_savefile, 'wb') as fp:
        pickle.dump(data, fp)


# ═════════════════════════════════════════════════════════════════════════════

def save_nights_to_file(data):
    path_to_savefile = os.path.join(
        config.PATH_TO_DATA_OUT, "nights", "nights.p")
    save_to_pickle(data, path_to_savefile)


def load_nights_from_file():
    path_to_savefile = os.path.join(
        config.PATH_TO_DATA_OUT, "nights", "nights.p")
    return load_from_pickle(path_to_savefile)

# ═════════════════════════════════════════════════════════════════════════════


def save_sleepnote_timeseries_to_file(data, sleepnote):
    path_to_savefile = os.path.join(
        PATH_TO_DATA_OUT, "sleep_notes", "timeseries", f"{sleepnote}.p"
    )
    with open(path_to_savefile, 'wb') as fp:
        pickle.dump(data, fp)


def load_sleepnote_timeseries_from_file(sn_name):
    path_to_savefile = os.path.join(
        PATH_TO_DATA_OUT, "sleep_notes", "timeseries", f"{sn_name}.p"
    )
    with open(path_to_savefile, 'rb') as fp:
        data = pickle.load(fp)
    return data

# ═════════════════════════════════════════════════════════════════════════════


def save_sleepnote_names_to_file(data):
    path_to_savefile = os.path.join(
        PATH_TO_DATA_OUT, "sleep_notes", f"names.json"
    )
    with open(path_to_savefile, 'w') as fp:
        json.dump(data, fp)


def load_sleepnote_names_from_file():
    path_to_savefile = os.path.join(
        PATH_TO_DATA_OUT, "sleep_notes", f"names.json"
    )
    with open(path_to_savefile, 'r') as fp:
        data = json.load(fp)
    return data

# ═════════════════════════════════════════════════════════════════════════════


def save_translated_sleepnote_names_to_file(data):
    path_to_savefile = os.path.join(
        PATH_TO_DATA_OUT, "sleep_notes", f"translated_names.json"
    )
    with open(path_to_savefile, 'w') as fp:
        json.dump(data, fp)


def load_translated_sleepnote_names_from_file():
    path_to_savefile = os.path.join(
        PATH_TO_DATA_OUT, "sleep_notes", f"translated_names.json"
    )
    with open(path_to_savefile, 'r') as fp:
        data = json.load(fp)
    return data


# ═════════════════════════════════════════════════════════════════════════════


def save_sleepcycle_usage_to_file(data):
    path_to_savefile = os.path.join(
        PATH_TO_DATA_OUT, "sleep_cycle", f"usage.p"
    )
    with open(path_to_savefile, 'wb') as fp:
        pickle.dump(data, fp)


def load_sleepcycle_usage_from_file():
    path_to_savefile = os.path.join(
        PATH_TO_DATA_OUT, "sleep_cycle", f"usage.p"
    )
    with open(path_to_savefile, 'rb') as fp:
        data = pickle.load(fp)
    return data

