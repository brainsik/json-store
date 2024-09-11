#!/usr/bin/env bash
set -e -x

tmp=$(mktemp tmpXXXXX)
uname -s
rm -f "$tmp"
python3 -c 'import shelve; db=shelve.open("'"$tmp"'", flag="n"); db["eggs"] = "eggs"; db.sync(); db.close()'

if [[ -s "$tmp".dat ]]; then
	# Windows
	shelve2json "$tmp".dat
elif [[ -s "$tmp".db ]]; then
	# macOS
	shelve2json "$tmp".db
else
	# Linux
	shelve2json "$tmp"
fi

rm -f "$tmp" "$tmp".{dat,db,json}
