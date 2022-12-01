#!/bin/sh

YELLOW='\033[1;33m'

path_to_remove=( 
    "../data/out/nights"
    "../data/out/time_series/sleep_notes"
    "../data/out/sleep_notes"
    "../figures.nosync/sleep_cycle" 
    "../figures.nosync/sleep_history" 
    "../figures.nosync/sleep_notes" 
)
echo
for path in "${path_to_remove[@]}"; do
    msg=" WARNING: Removing \"$path\""
    cd ./utils/cprint/bin && ./cprint "$msg" $YELLOW && cd ../../..
    rm -f "$path"/*
done
