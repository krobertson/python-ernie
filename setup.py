#!/usr/bin/env python

from distutils.core import setup
import bert

__version__ = bert.__version__


setup(
    name = 'ernie',
    version = __version__,
    description = 'BERT-Ernie Library',
    author = 'Ken Robertson',
    author_email = 'ken@invalidlogic.com',
    url = 'http://invalidlogic.com',
    packages = ['ernie'],
    classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
