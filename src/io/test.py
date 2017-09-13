#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is used to test each module.
"""

import read
# n, coord = read.configuration('qz.xyz')
# print n
# print coord
# print len(coord)

n, coord, nf = read.trajectory('qz.xyz')
print n
print coord
print nf
print len(coord[-1])
print coord[0][0][0]=='O'
