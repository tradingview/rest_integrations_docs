#!/bin/bash -e
source ./source.sh "$1"

"$1" -m pip install markupsafe==1.1.1
"$1" -m pip install jinja2==3.1.2
"$1" -m pip install sphinx==5.0.2
"$1" -m pip install beautifulsoup4
"$1" -m pip install lxml
"$1" -m pip install doc8
"$1" -m pip install -r requirements.txt