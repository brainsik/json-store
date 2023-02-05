#!/usr/bin/env bash
set -x -eu -o pipefail

if [ -z "${CI:-}" ]; then
	echo "This should only run under CI."
	exit 1
fi

# set all files to the VERSION timestamp
find . -type f -regextype egrep -regex '\./[^.].+' | xargs touch -r VERSION

# set system date/time to the VERSION timestamp
sudo timedatectl set-ntp no
sudo timedatectl set-time $(stat --format='%y' VERSION | grep -oP '\d\d\d\d-\d\d-\d\d')
sudo timedatectl set-time $(stat --format='%y' VERSION | grep -oP '\d\d:\d\d:\d\d')

python3 -m build
