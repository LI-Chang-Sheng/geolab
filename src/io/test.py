#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is used to test each module.
"""

from config import read
n, coord = read('qz.xyz')
print n
print coord
print len(coord)