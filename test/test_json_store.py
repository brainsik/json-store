# encoding: utf-8
from __future__ import absolute_import
from __future__ import unicode_literals

import os
import shutil
from tempfile import NamedTemporaryFile

try:
    import simplejson as json
except ImportError:
    import json

from nose.tools import assert_equal, assert_not_equal

import json_store


def get_new_store(json_kw=None):
    # get a random filename to use
    with NamedTemporaryFile(prefix=__name__ + ".") as f:
        path = f.name
    assert not os.path.exists(path), (
        "Tempfile was not deleted: %s" % path)

    store = json_store.open(path, json_kw)
    assert os.path.exists(path), "New store file was not created"
    return store


def test_empty_store():
    store = get_new_store()
    try:
        assert_equal(store, {})

        store2 = json_store.open(store.path)
        assert store2 is not store
        assert_equal(store2, store)
    finally:
        os.remove(store.path)


def test_store_stocking():
    store = get_new_store()
    try:
        assert_equal(store, {})
        store_copyfile = store.path + ".copy"

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


def test_kwargs_via_open():
    data = dict(monkey="gone to heaven")
    indented = json.dumps(data, indent=4)
    not_indented = json.dumps(data)

    store = get_new_store(json_kw=dict(indent=4))
    try:
        store.update(data)
        store.sync()

        with open(store.path, 'r') as fp:
            received = fp.read()
        assert_equal(indented, received)
        assert_not_equal(not_indented, received)
    finally:
        os.remove(store.path)


def test_kwargs_via_sync():
    data = dict(monkey="gone to heaven")
    indent4 = json.dumps(data, indent=4)

    store = get_new_store(json_kw=dict(indent=2))
    try:
        store.update(data)

        store.sync(json_kw=dict(indent=4))
        with open(store.path, 'r') as fp:
            received_indent4 = fp.read()
        assert_equal(indent4, received_indent4)

        store.sync()
        with open(store.path, 'r') as fp:
            received_indent2 = fp.read()
        assert_not_equal(indent4, received_indent2)
    finally:
        os.remove(store.path)
