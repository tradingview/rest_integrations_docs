#!/bin/bash -e
"$1" -m pip install sphinx==1.8.5
"$1" -m pip install beautifulsoup4
"$1" -m pip install lxml
"$1" -m pip install doc8
