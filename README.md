# json-store

[![json-store](https://github.com/brainsik/json-store/actions/workflows/main.yml/badge.svg)](https://github.com/brainsik/json-store/actions/workflows/main.yml)
![PyPI - json-store version](https://img.shields.io/pypi/v/json-store?v=4.6)
![PyPI - supported Python versions](https://img.shields.io/pypi/pyversions/json-store?v=4.6)

**json-store** is a simple replacement for shelve. It writes JSON serialized files,
accepts unicode keys, and tracks whether the store has been changed since last
sync. It has no dependencies.

json-store is intended for smaller stores. Everything is kept in memory and
`sync()` writes the whole store to disk.

For issues and development, see:

[https://github.com/brainsik/json-store](https://github.com/brainsik/json-store)
