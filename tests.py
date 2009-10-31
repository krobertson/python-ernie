#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import ernie

def sstr(str):
    return str

class TestModLoader(unittest.TestCase):
    def testMod(self):
        ernie.Ernie.mods.clear()
        ernie.mod('test')
        self.failUnlessEqual(ernie.Ernie.mods.keys(), ['test'])
        self.failUnlessEqual(ernie.mod('test').name, 'test')
    
    def testModFun(self):
        ernie.mod('test').funs.clear()
        ernie.mod('test').fun('sstr', sstr)
        self.failUnlessEqual(ernie.mod('test').funs.keys(), ['sstr'])
        self.failUnlessEqual(ernie.mod('test').funs['sstr'], sstr)

if __name__ == '__main__':
    unittest.main()
