[![json-store](https://github.com/brainsik/json-store/actions/workflows/main.yml/badge.svg)](https://github.com/brainsik/json-store/actions/workflows/main.yml)
![PyPI](https://img.shields.io/pypi/v/json-store)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/json-store)

# JSON Store

JSON store is a simple replacement for shelve. It writes JSON serialized files,
accepts unicode keys, and tracks whether the store has been changed since last
sync. It has no dependencies.

JSON store is intended for smaller stores. Everything is kept in memory and `sync()`
writes the whole store to disk.

For issues and development, see:

https://github.com/brainsik/json-store
