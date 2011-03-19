#! /usr/bin/env python
# encoding: utf-8
from __future__ import absolute_import
from __future__ import unicode_literals
"""Naïvely create a json_store file from a shelve DB."""

import os
import sys
import shelve

import json_store


def main(oldfile):
    if not os.path.isfile(oldfile):
        print "No such file:", oldfile
        raise SystemExit(1)

    data = shelve.open(oldfile)

    newfile = oldfile.rsplit(".db")[0] + ".json"
    store = json_store.open(newfile)
    store.update(data)
    store.sync()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Usage: {0[0]} <shelve.db>".format(sys.argv)
        raise SystemExit(1)
    main(sys.argv[1])
