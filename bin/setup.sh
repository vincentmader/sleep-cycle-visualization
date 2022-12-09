#!/bin/sh

#   Create virtual environment for python, if it does not exist already.
    [ -d ../venv ] || python3 -m venv ../venv

#   Install python requirements.
    ../venv/bin/pip3 install -r ../requirements.txt

#   Install colored-echo utility function.
    url="https://github.com/vincentmader/colored-echo.sh"
    target="./utils/cprint"
    [ -d $target ] || git clone $url $target
