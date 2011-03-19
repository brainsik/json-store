# encoding: utf-8
from __future__ import absolute_import
from __future__ import unicode_literals

import os
import shutil
from tempfile import NamedTemporaryFile

from nose.tools import assert_equal

import json_store


def get_new_store():
    # get a random filename to use
    with NamedTemporaryFile(prefix=__name__ + ".") as f:
        path = f.name
    assert not os.path.exists(path), (
        "Tempfile was not deleted: %s" % path)

    store = json_store.open(path)
    assert os.path.exists(path), "New store file was not created"
    return store


def test_empty_store():
    store = get_new_store()
    assert_equal(store, {})
    try:
        store2 = json_store.open(store.path)
        assert store2 is not store
        assert_equal(store2, store)
    finally:
        os.remove(store.path)


def test_store_stocking():
    store = get_new_store()
    assert_equal(store, {})

    store_copyfile = store.path + ".copy"
    try:
        store[u'\N{UMBRELLA}'] = 'umbrella'
        store.sync()
        assert_equal(len(store), 1)

        store['nested'] = [{'dict': {'a': None}}, u'\N{CLOUD}']
        store.sync()
        assert_equal(len(store), 2)

        shutil.copyfile(store.path, store_copyfile)
        store2 = json_store.open(store_copyfile)
        assert_equal(store2, store)
    finally:
        os.remove(store.path)
        if os.path.exists(store_copyfile):
            os.remove(store_copyfile)
