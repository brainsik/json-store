# encoding: utf-8
from distutils.core import setup

import json_store

setup(
    name='json-store',
    version=json_store.__version__,
    packages=['json_store'],
    entry_points={
        'console_scripts': [
            'shelve2json=json_store.shelve2json:main',
        ],
    },
    description="A shelve-like store using JSON serialization.",
    long_description="JSON store is a simple replacement for shelve. It writes"
                     " JSON serialized files, accepts unicode keys, and tracks"
                     " whether the store has been changed since last sync.",
    author='jeremy avnet',
    author_email='brainsik-code@theory.org',
    license='MIT License',
    url='https://github.com/brainsik/json-store',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
