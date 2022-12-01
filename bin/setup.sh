#!/bin/sh

#   Create virtual environment for python, if it does not exist already.
    [ -d ../venv ] || python3 -m venv ../venv

#   Install python requirements.
    ../venv/bin/pip3 install -r ../requirements.txt

#   Install colored-echo utility function.
    git clone https://github.com/vincentmader/colored-echo.sh ./utils/cprint

#   Create directory hierarchy.
    mkdir "../data/nights/"
    mkdir "../data/time_series/"
    mkdir "../data/time_series/sleep_notes/"
