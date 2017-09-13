#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import numpy as np
except ImportError:
    import warnings
    warnings.warn('Please install numpy if you plan to use'
                  'this module')

def read(filename=None, type='xyz'):
    """
    Currently support xyz format
    
    Read a configuration file named filename, and return a numpy array
    with element ['name', x, y, z]
    Parameter
    ----------
    filename: str
        filename or path to the file from which you want to load configration
    Return
    -------
     return: int number of atoms and a list [['atom', x, y, z],['atom', x, y, z]]
    """
    if type == 'xyz':
        coordinates = []
        xyz = open(filename, 'r')
        n_atoms = int(xyz.readline())
        title = xyz.readline()
        for line in xyz:
            if line.split()[0] =="%d\n"%n_atoms or line.split()[0] =="i" or line=="%s"%title:
                pass
            else:
                atom, x, y, z = line.split()
                coordinates.append([atom, float(x), float(y), float(z)])
        return n_atoms, np.array(coordinates)
    else:
        print "%s is not supported yet"%type
