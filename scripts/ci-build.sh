#!/usr/bin/env bash
set -x -eu -o pipefail

if [ -z "${CI:-}" ]; then
	echo "This should only run under CI."
	exit 1
fi

source BUILD.sh

# set all files to the VERSION timestamp
find . -type f -regextype egrep -regex '\./[^.].+' | xargs touch -r "$BUILD_TOUCH"

# set system date/time to the VERSION timestamp
date -R
sudo timedatectl set-ntp no
sudo timedatectl set-time "$BUILD_DATE"
sudo timedatectl set-time "$BUILD_TIME"
date -R

python3 -m build
