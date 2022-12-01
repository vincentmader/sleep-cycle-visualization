import config


def translate_sleepnote(sleepnote):
    if sleepnote in config.SLEEPNOTE_TRANSLATIONS.keys():
        return config.SLEEPNOTE_TRANSLATIONS[sleepnote]
    else:
        return sleepnote
