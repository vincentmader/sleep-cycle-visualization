from datetime import datetime as dt
from datetime import timedelta as td
import os
import pickle
from tqdm import tqdm

import config
from config import PATH_TO_DATA
from config import START_DATE
import utils
from utils.cprint import cprint
from data_preparation.sleep_notes.translation import translate_sleepnote
from data_preparation.sleep_notes.names import get_sleepnote_names


def prepare_empty_timeseries(sleepnotes):
    nr_of_days = (dt.now() - START_DATE).days
    days = [START_DATE + td(days=i) for i in range(nr_of_days)]
    timeseries = {}
    for sn in sleepnotes:
        sn = translate_sleepnote(sn)
        if sn not in timeseries.keys():
            timeseries[sn] = {d.timestamp(): None for d in days}
    return timeseries


def construct_sleepnote_timeseries_objects():
    nights = utils.file_io.load_nights_from_file()

    cprint("\n Constructing sleep-note time-series objects...")

    sleepnotes = utils.file_io.load_sleepnote_names_from_file()
    timeseries = prepare_empty_timeseries(sleepnotes)

    for night in nights:
        date = night.date
        for sleepnote in night.sleep_notes:
            if sleepnote in config.SLEEPNOTES_TO_SKIP:
                continue
            sleepnote = translate_sleepnote(sleepnote)
            timeseries[sleepnote][date.timestamp()] = True

    for sleepnote in tqdm(sleepnotes):
        sleepnote = translate_sleepnote(sleepnote)
        utils.file_io.save_sleepnote_timeseries_to_file(
            timeseries, sleepnote
        )

    translations = list(set([translate_sleepnote(sn) for sn in sleepnotes]))
    cprint(
        f" SUCCESS: Constructed time-series object for {len(sleepnotes)} -> {len(translations)} sleep-notes.", "green")

    return timeseries
