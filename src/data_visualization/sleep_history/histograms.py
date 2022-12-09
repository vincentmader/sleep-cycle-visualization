import os

import matplotlib.pyplot as plt

import config as cfg
from utils.file_io import load_from_pickle

PATH_TO_HISTORY = os.path.join(cfg.PATH_TO_DATA_OUT, "sleep_history")
PATH_TO_FIGURES = os.path.join(cfg.PATH_TO_FIGURES, "sleep_history", "histograms")

TITLES = {
    "measurement_start": "measurement start-time [h]",
    "measurement_end": "measurement end-time [h]",
    "sleep_start": "sleep start-time [h]",
    "sleep_end": "sleep end-time [h]",
    "time_asleep_in_h": "time asleep [h]",
    "time_before_sleep_in_h": "time before sleep [h]",
    "sleep_quality": "sleep quality",
    "nr_of_steps": "nr. of steps",
    "nr_of_moves_per_h": "nr. of moves per hour",
    "heart_rate": "heart rate",
    "snore_time": "snore time [?]",
    "weather_temp_in_c": "weather temperature [deg. C]",
    "wakeup_mood": "mood at wake-up",
    "air_pressure_in_pa": "air pressure [Pa]",
    "measurement_duration_in_h": "measurement duration [h]",
    "sleep_regularity": "sleep regularity",
}
DATASET_NAMES = [
    "measurement_start",
    "measurement_end",
    "sleep_start",
    "sleep_end",
    "time_asleep_in_h",
    "time_before_sleep_in_h",
    "sleep_quality",
    "nr_of_steps",
    "nr_of_moves_per_h",
    "heart_rate",
    "snore_time",
    "weather_temp_in_c",
    "wakeup_mood",
    "air_pressure_in_pa",
    "measurement_duration_in_h",
    "sleep_regularity",
]
NAMES_A = [
    "measurement_start",
    "measurement_end",
    "sleep_start",
    "sleep_end",
]
NAMES_B = [
    "time_asleep_in_s",
    "time_before_sleep_in_s",
    "nr_of_steps",
    "nr_of_moves_per_h",
    "heart_rate",
    "snore_time",
    "weather_temp_in_c",
    "air_pressure_in_pa",
    "measurement_duration_in_s",
]
NAMES_C = [
    "wakeup_mood",
]
NAMES_D = [
    "sleep_quality",
    "sleep_regularity",
]


def plot_histograms():
    for dataset_name in DATASET_NAMES:
        filename = f"{dataset_name}.p"
        path_to_savefile = os.path.join(PATH_TO_HISTORY, filename)
        timeseries = load_from_pickle(path_to_savefile)

        if dataset_name in NAMES_A:
            hours = range(24)
            histogram = { h: 0 for h in hours } 
            values = [v for v in timeseries.values if v != None]
            for i in values:
                histogram[i.hour] += 1

            x = sorted(histogram.keys())
            y = [histogram[i] for i in x]
            plt.bar(x, y)
            
            plt.xlim(x[0] - 0.5, x[-1] + 0.5)
            xtick_locs = range(0, 24+1, 3)
            xtick_labels = [
                f"0{i}:00" if i < 10 else f"{i}:00"
                for i in xtick_locs
            ]
            plt.xticks(xtick_locs, xtick_labels)
            plt.xlabel("time")
            plt.ylabel("count")

        elif dataset_name in NAMES_B:
            x = timeseries.values
            x = [i for i in x if i != None]
            plt.hist(x, bins=50)

        elif dataset_name in NAMES_C:
            x = timeseries.values
            x = [i for i in x if i != None]
            plt.hist(x, bins=3)

        elif dataset_name in NAMES_D:
            x = timeseries.values
            x = [i for i in x if i != None]
            plt.hist(x, bins=100)

        else:
            continue
        
        plt.title(TITLES[dataset_name])

        filename = f"{dataset_name}.png"
        path_to_savefile = os.path.join(PATH_TO_FIGURES, filename)
        plt.savefig(path_to_savefile)
        # plt.show()
        plt.close()
