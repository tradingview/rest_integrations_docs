#!/bin/bash -x
PWD=`pwd`

"$1" -m venv venv

echo $PWD

activate () {
	. $PWD/venv/bin/activate
}

activate

make html
"$1" processLink.py