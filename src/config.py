from datetime import datetime as dt
import json
import os

START_DATE = dt(2013, 1, 1)

MPL_THEME = "~/.config/matplotlib/dark.mplstyle"

PATH_TO_DATA_IN = "../in.nosync"
PATH_TO_DATA_OUT = os.path.join("../out.nosync", "data")
PATH_TO_FIGURES = os.path.join("../out.nosync", "figures")
PATH_TO_SC_EXPORTS = os.path.join(PATH_TO_DATA_IN, "exports")

path = os.path.join(PATH_TO_DATA_IN, "sleepnote_translations.json")
with open(path) as fp:
    SLEEPNOTE_TRANSLATIONS = json.load(fp)

path = os.path.join(PATH_TO_DATA_IN, "sleepnotes_to_skip.json")
with open(path) as fp:
    SLEEPNOTES_TO_SKIP = json.load(fp)

