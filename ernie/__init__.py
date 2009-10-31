
"""BERT-ERNIE Library"""

__version__ = "0.0.1"

import bert
from ernie import Ernie, Mod

def mod(name):
    return Ernie.mod(name)

def start():
    server = Ernie()
    server.start()