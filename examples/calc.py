#!/usr/bin/env python

from ernie import mod, start
from ernie import Ernie
from time import sleep


def calc_add(a, b):
    return a + b

def slowcalc_add(a,b):
    sleep(2)
    return a + b

def slowcalc_superslow():
    sleep(10)

def errorcalc_add(a,b):
    raise Exception("oops!")

mod('calc').fun('add', calc_add)
mod('slowcalc').fun('add', slowcalc_add)
mod('slowcalc').fun('superslow', slowcalc_superslow)
mod('errorcalc').fun('add', errorcalc_add)

if __name__ == "__main__":
    start()
