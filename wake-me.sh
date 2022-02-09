#!/usr/bin/bash

if [[ $* == *--wait* || $* == *-w* ]]; then
    /home/tubbadu/code/GitHub/wake-me/wake-me.py "$@"
else
    /home/tubbadu/code/GitHub/wake-me/wake-me.py "$@" & sleep 0.1
fi