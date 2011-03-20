# encoding: utf-8
from distutils.core import setup

setup(
    name='json-store',
    version='1.1',
    packages=['json_store',],
    scripts=['bin/shelve2json.py',],
    description="A shelve-like store using JSON serialization.",
    long_description="JSON store is a simple replacement for shelve. It writes"
                     " JSON serialized files and can accept unicode keys.",
    author='jeremy avnet',
    author_email='brainsik-code@theory.org',
    license='MIT License',
    url='https://github.com/brainsik/json-store',
    download_url='http://pypi.python.org/packages/source/j/json-store/json-store-1.1.tar.gz',
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2.6',]
)
