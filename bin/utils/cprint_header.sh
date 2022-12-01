#!/bin/sh

msg=""
msg="$msg ╔═══════════════════════════════════════════╗\n"
msg="$msg ║ SLEEP-CYCLE DATA ANALYSIS & VISUALIZATION ║\n"
msg="$msg ╚═══════════════════════════════════════════╝"

color="blue"

clear
cd ./cprint/bin && ./cprint "$msg" "$color"
