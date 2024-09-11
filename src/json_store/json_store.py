# encoding: utf-8
"""A JSON store to use in place of shelve. Unicode keys, FTW!

This is for small stores. Everything is in memory and sync() always writes
everything out to disk.
"""
import json
import os
from collections.abc import MutableMapping
from tempfile import NamedTemporaryFile

__all__ = ["JSONStore"]

MODE_600 = int("600", 8)


class JSONStore(MutableMapping):
    def __init__(self, path, json_kw=None, mode=MODE_600):
        """Create a JSONStore object backed by the file at `path`.

        If a dict is passed in as `json_kw`, it will be used as keyword
        arguments to the json module.
        """
        self.path = path
        self.json_kw = json_kw or {}
        self.mode = mode

        self._data = {}

        self._synced_json_kw = None
        self._needs_sync = False

        if not os.path.exists(path):
            self.sync(force=True)  # write empty dict to disk
            return

        # load the whole store
        with open(path, "r") as fp:
            self.update(json.load(fp))

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value
        self._needs_sync = True

    def __delitem__(self, key):
        del self._data[key]
        self._needs_sync = True

    def keys(self):
        return self._data.keys()

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def _mktemp(self):
        prefix = os.path.basename(self.path) + "."
        dirname = os.path.dirname(self.path)
        return NamedTemporaryFile(mode="w", prefix=prefix, dir=dirname, delete=False)

    def sync(self, json_kw=None, force=False):
        """Atomically write the entire store to disk if it's changed.

        If a dict is passed in as `json_kw`, it will be used as keyword
        arguments to the json module.

        If force is set True, a new file will be written even if the store
        hasn't changed since last sync.
        """
        json_kw = json_kw or self.json_kw
        if self._synced_json_kw != json_kw:
            self._needs_sync = True

        if not (self._needs_sync or force):
            return False

        with self._mktemp() as fp:
            json.dump(self._data, fp, **json_kw)
        if self.mode != MODE_600:  # _mktemp uses 0600 by default
            os.chmod(fp.name, self.mode)
        os.replace(fp.name, self.path)

        self._synced_json_kw = json_kw
        self._needs_sync = False
        return True
