# encoding: utf-8
"""A JSON store to use in place of shelve. Unicode keys, FTW!

This is for small stores. Everything is in memory and sync() always writes
everything out to disk.
"""
from __future__ import absolute_import
from __future__ import unicode_literals

__version__ = "1.0"

try:
    import simplejson as json
except ImportError:
    import json

import os
import shutil
from tempfile import NamedTemporaryFile

_open = open  # gets overwritten later


class JSONStore(dict):

    def __init__(self, path):
        self.path = path

        if not os.path.exists(path):
            self.sync()  # write empty dict to disk
            return

        # load the whole store
        with _open(path, 'r') as fp:
            self.update(json.load(fp))

    def _mktemp(self):
        prefix = os.path.basename(self.path) + "."
        dirname = os.path.dirname(self.path)
        return NamedTemporaryFile(prefix=prefix, dir=dirname, delete=False)

    def sync(self):
        """Atomically write the entire store to disk."""
        fp = None
        try:
            with self._mktemp() as fp:
                json.dump(self, fp)
            shutil.copyfile(fp.name, self.path)
        finally:
            if fp:
                os.remove(fp.name)


def open(path):
    return JSONStore(path)
