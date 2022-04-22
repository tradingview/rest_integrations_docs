#!/bin/bash -x
source ./source.sh "$1"
make html
"$1" processLink.py