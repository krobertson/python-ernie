#!/usr/bin/env python

from distutils.core import setup

from bert import __version__ as version

setup(
    name = 'ernie',
    version = version,
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
