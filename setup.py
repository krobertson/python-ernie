#!/usr/bin/env python

from distutils.core import setup
from bert import __version__ as version

__version__ = version

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
    install_requires = ["bert>=2.0.0"],
	dependency_links = [
		'http://github.com/samuel/python-bert/tarball/master#egg=bert-2.0.0'
	]
)
