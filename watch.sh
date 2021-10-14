#!/bin/bash

# initial build
make doc

# kill all subshells and processes on exit
trap "kill 0" SIGINT

# start commands in subshells so all their spawn die when we exit
( "$1" -m http.server 8000 -d build/html ) &
( npx watch-cli -p "**/*.rst" -c "make doc" ) &
wait
