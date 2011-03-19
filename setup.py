# encoding: utf-8
from distutils.core import setup

setup(
    name='json-store',
    version='1.0',
    packages=['json_store',],
    scripts=['bin/shelve2json.py',],
    license='MIT License',
    description="A shelve-like store using JSON serialization.",
    long_description="A JSON store to use in place of shelve.",
    author='jeremy avnet',
    author_email='brainsik-code@theory.org',
    url='https://github.com/brainsik/brainsik',
)
