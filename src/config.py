from datetime import datetime as dt
import json
import os

PATH_TO_DATA = "../data/"
PATH_TO_SC_EXPORTS = os.path.join(PATH_TO_DATA, "exports")
PATH_TO_FIGURES = "../figures"

START_DATE = dt(2012, 1, 1)

path_to_sleepnote_translations= os.path.join(PATH_TO_DATA, "sleepnote_translations.json")
with open(path_to_sleepnote_translations) as fp:
    SLEEPNOTE_TRANSLATIONS = json.load(fp)

path_to_sleepnotes_to_skip= os.path.join(PATH_TO_DATA, "sleepnotes_to_skip.json")
with open(path_to_sleepnotes_to_skip) as fp:
    SLEEPNOTES_TO_SKIP = json.load(fp)
