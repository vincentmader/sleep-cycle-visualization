#!/bin/sh

YELLOW='\033[1;33m'

path_to_remove=( 
    "../out.nosync/"
)
echo
for path in "${path_to_remove[@]}"; do
    msg=" Removing \"$path\"..."
    cd ./utils/cprint/bin && ./cprint "$msg" $YELLOW && cd ../../..
    rm -rf "$path"/*
done
