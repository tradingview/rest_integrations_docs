#!/bin/bash -x
PWD=`pwd`

"$1" -m venv venv

echo $PWD

activate () {
	. $PWD/venv/bin/activate
}

activate
