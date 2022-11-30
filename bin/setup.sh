#!/bin/sh

#   Create virtual environment for python, if it does not exist already.
    [ -d ../venv ] || python3 -m venv ../venv

#   Install python requirements.
    ../venv/bin/pip3 install -r ../requirements.txt

#   Create directory hierarchy.
    cd "../data/nights/"
    cd "../data/time_series/"
    cd "../data/time_series/sleep_notes/"
    cd "../figures/Sleep-Note Usage vs. Time (moving avg.)/"