import os

import matplotlib.pyplot as plt

import config
from config import PATH_TO_FIGURES


def plot_sleep_snake():
    path_to_savefile = os.path.join(
        PATH_TO_FIGURES, "sleep_history", "sleep_snake.png"
    )
