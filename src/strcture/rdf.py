#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file is used to calculate rdf

"""
def rdf(config=None, center='O', neighbor='H', max=10, binsize=0.1,plt=True):
    """
    calculate RDF from a configuration.

    RDF from a trajectory will be implemented soon.

    Parameters
    ----------
    config: str
        configure file name
    center:  str
        center atom symbol
    neighbor: str
        neighbor atom symbol
    max: float
        max distance for rdf
    binsize: float
        rdf bin size
    plt: bool
        whether or not to plot it out

    Returns
    -------
    return, a file named config-center-neihbor-rdf-max-bin.dat in which rdf data are written

    """

    return 'not implemeted yet'
