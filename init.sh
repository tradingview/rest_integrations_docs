#!/bin/bash -e
"$1" -m pip install markupsafe==1.1.1
"$1" -m pip install jinja2==2.10.1
"$1" -m pip install sphinx==1.8.5
"$1" -m pip install beautifulsoup4
"$1" -m pip install lxml
"$1" -m pip install doc8
