#!/usr/bin/env python
from __future__ import print_function
import unittest
import tbin

class TestTbin(unittest.TestCase):
    def test_init(self):
        pass
    
    def test_getValue(self):
        self.assertEquals(tbin.getValue(0,101),0)
        self.assertEquals(tbin.getValue(0,156),1)
        self.assertEquals(tbin.getValue(1,179),0)


if __name__ == '__main__':
    unittest.main()
