#! /usr/bin/env python
# encoding: utf-8
from __future__ import absolute_import
from __future__ import unicode_literals
"""Naïvely create a json_store file from a shelve DB."""

import os
import sys
import shelve

import json_store


def convert(oldfile):
    if not os.path.isfile(oldfile):
        print "No such file:", oldfile
        raise SystemExit(1)

    data = shelve.open(oldfile)

    newfile = oldfile.rsplit(".db")[0] + ".json"
    store = json_store.open(newfile)
    store.update(data)
    store.sync()


def main(argv):
    if len(argv) < 2:
        print "Usage: {0[0]} <shelve.db>".format(sys.argv)
        return 1

    convert(argv[1])


if __name__ == '__main__':
    sys.exit(main(sys.argv))
