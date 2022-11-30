import os
import pickle

import config


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


def save_nights_to_file(nights):
    path_to_savefile = os.path.join(config.PATH_TO_DATA, "nights", "nights.p")
    save_to_pickle(nights, path_to_savefile)


def load_nights_from_file():
    path_to_savefile = os.path.join(config.PATH_TO_DATA, "nights", "nights.p")
    return load_from_pickle(path_to_savefile)
