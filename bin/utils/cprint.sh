#!/bin/sh

msg="$1"

nocolor="\033[0m"

color="$2"

if [[ "$color" == "black" ]]; then
    color="\033[0;30m"
elif [[ "$color" == "red" ]]; then
    color="\033[0;31m"
elif [[ "$color" == "green" ]]; then
    color="\033[0;32m"
elif [[ "$color" == "orange" ]]; then
    color="\033[0;33m"
elif [[ "$color" == "blue" ]]; then
    color="\033[0;34m"
elif [[ "$color" == "purple" ]]; then
    color="\033[0;35m"
elif [[ "$color" == "cyan" ]]; then
    color="\033[0;36m"
elif [[ "$color" == "lightgray" ]]; then
    color="\033[0;37m"
elif [[ "$color" == "darkgray" ]]; then
    color="\033[1;30m"
elif [[ "$color" == "lightred" ]]; then
    color="\033[1;31m"
elif [[ "$color" == "lightgreen" ]]; then
    color="\033[1;32m"
elif [[ "$color" == "yellow" ]]; then
    color="\033[1;33m"
elif [[ "$color" == "lightblue" ]]; then
    color="\033[1;34m"
elif [[ "$color" == "lightcyan" ]]; then
    color="\033[1;35m"
elif [[ "$color" == "lightcyan" ]]; then
    color="\033[1;36m"
elif [[ "$color" == "white" ]]; then
    color="\033[1;37m"
fi

echo $color$msg$nocolor
