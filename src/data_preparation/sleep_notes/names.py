import config
from data_preparation.sleep_notes.translation import translate_sleepnote
from utils.file_io import load_sleepnote_names_from_file
from utils.file_io import load_nights_from_file
from utils.file_io import save_sleepnote_names_to_file
from utils.file_io import save_translated_sleepnote_names_to_file


def get_sleepnote_names():
    nights = load_nights_from_file()
    names = []
    for night in nights:
        names += [
            sn for sn in night.sleep_notes
            if sn not in names
            and sn not in config.SLEEPNOTES_TO_SKIP
        ]
    save_sleepnote_names_to_file(names)


def get_translated_sleepnote_names():
    names = load_sleepnote_names_from_file()
    translated = [translate_sleepnote(sn) for sn in names]
    save_translated_sleepnote_names_to_file(translated)
