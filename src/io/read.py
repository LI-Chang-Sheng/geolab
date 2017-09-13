#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import numpy as np
except ImportError:
    import warnings
    warnings.warn('Please install numpy if you plan to use'
                  'this module')


def configuration(filename=None, type='xyz'):
    """
    Currently support xyz format only.
    
    The extended XYZ format will be implemented soon.

    Read a configuration file named filename, and return a numpy array
    with element ['name', x, y, z]
    
    Parameters
    -----------
    filename: str
        filename or path to the file from which you want to load configration
    
    Returns
    --------
    return: int
        number of atoms
        
    return: ndarray
        name and positions
    
    """
    if filename == None:
        import warnings
        warnings.warn('No file provided.')
    else:
        pass
    if type == 'xyz':
        coordinates = []
        xyz = open(filename, 'r')
        n_atoms = int(xyz.readline())
        title = xyz.readline()
        for line in xyz:
            if line.split()[0] == "%d\n" % n_atoms or line.split()[0] == "i" or line == "%s" % title:
                pass
            else:
                atom, x, y, z = line.split()
                coordinates.append([atom, float(x), float(y), float(z)])
        return n_atoms, np.array(coordinates)
    else:
        print "%s is not supported yet" % type


def trajectory(filename=None, type='xyz'):
    """
    Currently support xyz file only.
    
    The extended XYZ format will be implemented soon.
    
    Read a trajectory file and split it by frames.
    
    Parameters
    ----------
    filename: str
        filename or path to your trajectory file
    
    type: str
        trajectory type, default is xyz

    Returns
    -------
    n_atoms: int
        how many atoms do you have
        
    coordinations: numpy array
        an array of frames, and each frame is consisted of n_atoms atoms.
        
    n_frams: int
        how many frames do you have

    """
    if filename==None:
        import warnings
        warnings.warn('No file provided.')
    coordinates = []
    xyz = open(filename)
    n_atoms = int(xyz.readline())
    title = xyz.readline()
    for line in xyz:
        if line.split()[0] == "%d\n" % n_atoms or line.split()[0] == "i" or line == "%s" % title:
            pass
        else:
            atom, x, y, z = line.split()
            coordinates.append([atom, float(x), float(y), float(z)])
    xyz.close()
    filelines = len(coordinates)
    nframe = filelines / n_atoms
    coordinatesframes = []
    for i in range(nframe):
        istart = i * n_atoms
        iend = (i + 1) * n_atoms
        coordinatesframes.append(coordinates[istart:iend])
    return n_atoms, np.array(coordinatesframes), nframe