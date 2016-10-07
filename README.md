[![Build Status](https://api.travis-ci.org/brainsik/json-store.svg?branch=master)](https://travis-ci.org/brainsik/json-store)

# JSON Store

JSON store is a simple replacement for shelve. It writes JSON serialized files,
accepts unicode keys, and tracks whether the store has been changed since last
sync.

Note, JSON store is intended for small stores. Everything is in memory and
sync() writes the whole store to disk.

For issues and development, see it's github page:

https://github.com/brainsik/json-store
