#!/bin/sh
set -e -x

tmp=$(mktemp)
rm -f "$tmp"
python -c 'import shelve; db=shelve.open("'"$tmp"'", flag="n"); db["eggs"] = "eggs"; db.close()'
shelve2json "$tmp"
rm -f "$tmp" "$tmp.json"
