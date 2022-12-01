from config import SLEEPNOTE_TRANSLATIONS
from config import SLEEPNOTES_TO_SKIP
from utils.file_io import load_sleepnote_names_from_file
from utils.file_io import load_nights_from_file
from utils.file_io import save_sleepnote_names_to_file
from utils.file_io import save_translated_sleepnote_names_to_file


def get_sleepnote_names():
    """Get a list of all sleep-note names used in the SleepCycle exports."""

    nights = load_nights_from_file()

    names = []
    for night in nights:
        names += [
            sn for sn in night.sleep_notes
            if sn not in names
            and sn not in SLEEPNOTES_TO_SKIP
        ]

    save_sleepnote_names_to_file(names)
    return names


def get_translated_sleepnote_names():
    """Get a list of all "translated "sleep-note names."""

    names = load_sleepnote_names_from_file()

    translated = [translate_sleepnote(sn) for sn in names]
    translated = list(set(translated))

    save_translated_sleepnote_names_to_file(translated)
    return translated


def translate_sleepnote(sleepnote):
    """"Translate" a sleep-note into nicer formulation."""

    if sleepnote in SLEEPNOTE_TRANSLATIONS:
        return SLEEPNOTE_TRANSLATIONS[sleepnote]
    else:
        return sleepnote
