#! /usr/bin/env python
# encoding: utf-8
"""Naïvely create a json_store file from a shelve DB."""

import os
import shelve
import sys

import json_store


def convert(oldfile: str):
    if not os.path.isfile(oldfile):
        raise ValueError("No such file: {}".format(oldfile))

    name = oldfile
    # remove extensions that are implicitly added by the underlying DBM module
    if name.endswith(".dat"):  # Windows
        name = name.rsplit(".dat", 1)[0]
    if name.endswith(".db"):  # macOS
        name = name.rsplit(".db", 1)[0]

    newfile = name + ".json"
    store = json_store.open(newfile)
    with shelve.open(name) as data:
        store.update(data)
    store.sync()


def main(argv=sys.argv):
    if len(argv) < 2:
        print("Usage: {0[0]} <shelve_db>".format(sys.argv))
        return 1

    try:
        convert(argv[1])
    except Exception as e:
        print(str(e), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
