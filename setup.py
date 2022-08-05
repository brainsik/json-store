# encoding: utf-8
import setuptools

import json_store

setuptools.setup(
    name="json-store",
    version=json_store.__version__,
    packages=["json_store"],
    entry_points={
        "console_scripts": [
            "shelve2json=json_store.shelve2json:main",
        ],
    },
    description="A shelve-like store using JSON serialization.",
    long_description=(
        "JSON store is a simple replacement for shelve. It writes"
        " JSON serialized files, accepts unicode keys, and tracks"
        " whether the store has been changed since last sync."
    ),
    author="jeremy avnet",
    author_email="brainsik-code@theory.org",
    license="MIT License",
    url="https://github.com/brainsik/json-store",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
