#!/bin/sh

YELLOW='\033[1;33m'

path_to_remove=( 
    "../data/nights/*"
    "../data/time_series/sleep_notes/*"
    "../figures/Sleep-Note Usage vs. Time (moving avg.)/*" 
)
echo
for path in "${path_to_remove[@]}"; do
    msg=" WARNING: Removing \"$path\""
    ./utils/cprint.sh "$msg" $YELLOW
    rm -f "$path"
done
