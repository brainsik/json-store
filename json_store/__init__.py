# encoding: utf-8
"""A JSON store to use in place of shelve. Unicode keys, FTW!

This is for small stores. Everything is in memory and sync() always writes
everything out to disk.
"""
from __future__ import absolute_import
from __future__ import unicode_literals

__version__ = "1.1"

import __builtin__
import os
import shutil
from tempfile import NamedTemporaryFile

try:
    import simplejson as json
except ImportError:
    import json


class JSONStore(dict):

    def __init__(self, path, json_kw=None):
        """Create a JSONStore object backed by the file at `path`.

        If a dict is passed in as `json_kw`, it will be used as keyword
        arguments to the json module.
        """
        self.path = path
        self.json_kw = json_kw or {}

        if not os.path.exists(path):
            self.sync()  # write empty dict to disk
            return

        # load the whole store
        with __builtin__.open(path, 'r') as fp:
            self.update(json.load(fp))

    def _mktemp(self):
        prefix = os.path.basename(self.path) + "."
        dirname = os.path.dirname(self.path)
        return NamedTemporaryFile(prefix=prefix, dir=dirname, delete=False)

    def sync(self, json_kw=None):
        """Atomically write the entire store to disk.

        If a dict is passed in as `json_kw`, it will be used as keyword
        arguments to the json module.
        """
        fp = None
        json_kw = json_kw or self.json_kw
        try:
            with self._mktemp() as fp:
                json.dump(self, fp, **json_kw)
            shutil.copyfile(fp.name, self.path)
        finally:
            if fp:
                os.remove(fp.name)


def open(path, json_kw=None):
    return JSONStore(path, json_kw)
