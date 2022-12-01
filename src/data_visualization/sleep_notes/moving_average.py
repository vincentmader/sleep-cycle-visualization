from utils.cprint import cprint
from utils.file_io import load_sleepnote_timeseries_from_file
from utils.file_io import load_sleepnote_names_from_file


def plot_moving_average():
    cprint("\n Plotting sleep-note moving-averages...")

    sleepnote_names = load_sleepnote_names_from_file()
    


